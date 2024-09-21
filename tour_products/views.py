from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import TourProducts
from .forms import TourForm, TourImage


def all_tours(request):
    ''' A view that shows all tours & Allows search bar function'''

    tourproducts = TourProducts.objects.all()
    query = None

    # Search bar queryS
    if request.GET:
        if 's-q' in request.GET:
            query = request.GET['s-q']
            if not query:
                messages.error(request, "Invalid search criteria")
                return redirect(reverse('all-tours'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            tourproducts = tourproducts.filter(queries)

    # Getting categories 
    categories = tourproducts.values_list('category', flat=True).distinct()

    selected_category = request.GET.get('category', None)
    if selected_category:
        tourproducts = tourproducts.filter(category__iexact=selected_category)

    context = {
        'tourproducts': tourproducts,
        'search_text': query,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'tours/tour_products.html', context)


def tour_breakdown(request, tour_id):
    ''' View that shows individual tour breakdown '''

    tour = get_object_or_404(TourProducts, pk=tour_id)
    tour_images = TourImage.objects.filter(tour=tour)

    context = {
        'tour': tour,
        'tour_images': tour_images,
    }

    return render(request, 'tours/tour_breakdown.html', context)


@login_required
def add_tour(request):
    """ Add a tour to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only ADMINS users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            new_tour = form.save()

            # Handle multiple images upload
            images = request.FILES.getlist('images')
            for image in images:
                TourImage.objects.create(tour=new_tour, image=image)

            # Only show success message once after adding the tour and images
            messages.success(request, 'Successfully added new TOUR!')

            return redirect(reverse('tour-breakdown', args=[new_tour.id]))
        else:
            messages.error(request, 'Failed to add tour. Please ensure the form is valid.')
    else:
        form = TourForm()

    template = 'tours/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tour(request, tour_id):
    """ Edit a tour """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only ADMINS users can do that.')
        return redirect(reverse('home'))

    tour = get_object_or_404(TourProducts, pk=tour_id)

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        images = request.FILES.getlist('images')

        if form.is_valid():
            form.save()

            for image in images:
                TourImage.objects.create(tour=tour, image=image)

            messages.success(request, 'Successfully updated Tour!')
            return redirect(reverse('tour-breakdown', args=[tour.id]))
        else:
            messages.error(request, 'Failed to update tour. Please ensure the form is valid.')
    else:
        form = TourForm(instance=tour)
        messages.info(request, f'You are editing {tour.name}')

    template = 'tours/edit_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }

    return render(request, template, context)

    """ Edit a tour """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only ADMINS users can do that.')
        return redirect(reverse('home'))

    tour = get_object_or_404(TourProducts, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Tour!')
            return redirect(reverse('tour-breakdown', args=[tour.id]))
        else:
            messages.error(request, 'Failed to update tour. Please ensure the form is valid.')
    else:
        form = TourForm(instance=tour)
        messages.info(request, f'You are editing {tour.name}')

    template = 'tours/edit_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }

    return render(request, template, context)


@login_required
def delete_tour(request, tour_id):
    """ Delete a tour from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only ADMINS users can do that.')
        return redirect(reverse('home'))

    tour = get_object_or_404(TourProducts, pk=tour_id)
    tour.delete()
    messages.success(request, 'Tour deleted!')
    return redirect(reverse('all-tours'))
