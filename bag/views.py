from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from tour_products.models import TourProducts


def view_bag(request):
    """ Returns view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_backpack(request, item_id):
    """ Add tour to backpack """

    tour = TourProducts.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Get varible if already extists if not creates one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity if exsists
        bag[item_id] += quantity
        messages.success(
            request, f'Added {tour.name} tour to your travel backpack')

    else:
        # Add to bag
        bag[item_id] = quantity
        messages.success(
            request, f'Added {tour.name} tour to your travel backpack')

    # Update/create bag on session
    request.session['bag'] = bag
    return redirect(redirect_url)


def modify_backpack(request, item_id):
    """ Modify the quantity on the tour to a certain amount """

    quantity = int(request.POST.get('quantity'))

    # Get varible if already extists if not creates one
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    # Update/create bag on session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
