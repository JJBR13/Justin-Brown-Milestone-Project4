from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from tour_products.models import TourProducts

def view_bag(request):
    """ Returns view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_backpack(request, item_id):
    """ Add tour to backpack """

    tour = TourProducts.objects.get(pk=item_id)
    # quantity = int(request.POST.get('quantity'))  # Commenting out quantity
    redirect_url = request.POST.get('redirect_url')

    # Get varible if already exists, if not creates one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity if exists
        # bag[item_id] += quantity  # Commenting out quantity logic
        messages.success(
            request, f'Added {tour.name} tour to your travel backpack')

    else:
        # Add to bag without quantity
        # bag[item_id] = quantity  # Commenting out quantity logic
        bag[item_id] = 1  # Default to 1 as there is no quantity logic now
        messages.success(
            request, f'Added {tour.name} tour to your travel backpack')

    # Update/create bag on session
    request.session['bag'] = bag
    return redirect(redirect_url)

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
    
def update_backpack(request, item_id):
    """ Modify the quantity on the tour to a certain amount """

    quantity = int(request.POST.get('quantity'))

    # Get varible if already extists if not creates one
    bag = request.session.get('bag', {})

    url = reverse('update_backpack', args=[item_id])
    
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    # Update/create bag on session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_backpack(request, item_id):
    """Remove the tour product from the backpack."""

    try:
        bag = request.session.get('bag', {})

        # Check if the item exists in the bag
        if str(item_id) in bag:
            # Remove the item from the bag
            bag.pop(str(item_id))
            # Update the session bag
            request.session['bag'] = bag
            return HttpResponse(status=200)
        else:
            # If item is not found in the bag, return a 404 response
            return HttpResponse(status=404, reason='Item not found in the backpack')

    except Exception as e:
        # Log the exception if needed, and return a 500 response
        return HttpResponse(status=500, reason=str(e))
