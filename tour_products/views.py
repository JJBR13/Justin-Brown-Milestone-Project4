from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import TourProducts
from .forms import TourForm


def all_tours(request):
    ''' A view that shows all tours & Allows search bar function'''

    tourproducts = TourProducts.objects.all()
    query = None

    # Search bar queryS
    if request.GET:
        if 's-q' in request.GET:
            query = request.GET['sq']
            if not query:
                messages.error(request, "Invalid search criteria")
                return redirect(reverse('all-tours'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            tourproducts = tourproducts.filter(queries)

    context = {
        'tourproducts': tourproducts,
        'search_text': query,
    }

    return render(request, 'tours/tour_products.html', context)


def tour_breakdown(request, tour_id):
    ''' View that shows individual tour breakdown '''

    tour = get_object_or_404(TourProducts, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_breakdown.html', context)

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import TourForm

def add_tour(request):
    """ Add a tour to site """
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new TOUR!')
            return redirect(reverse('add_tour'))
        else:
            messages.error(request, 'Failed to add tour. Please ensure the form is valid.')
    else:
        form = TourForm()

    template = 'tours/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
