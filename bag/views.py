from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from tour_products.models import TourProducts

def view_bag(request):
    """ Returns view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_backpack(request, item_id):
    """ Add tour to backpack """

    try:
        # Fetch the tour by primary key
        tour = TourProducts.objects.get(pk=item_id)
        redirect_url = request.POST.get('redirect_url')
        
        # Initialize bag session variable
        bag = request.session.get('bag', {})

        if item_id in bag:
            # If item already in bag, update message without changing quantity
            messages.success(request, f'Added {tour.name} tour to your travel backpack')
        else:
            # Add to bag with initial quantity of 1
            bag[item_id] = 1
            messages.success(request, f'Added {tour.name} tour to your travel backpack')

        # Save the updated bag to session
        request.session['bag'] = bag
        return redirect(redirect_url)
    except TourProducts.DoesNotExist:
        messages.error(request, "Tour not found.")
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('view_bag')

def update_backpack(request, item_id):
    """ Modify the quantity of the tour in the backpack. """
    try:
        quantity = int(request.POST.get('quantity', 0))
        tour = TourProducts.objects.get(pk=item_id)

        # Get the session bag or create an empty one if it doesn't exist
        bag = request.session.get('bag', {})

        if quantity > 0:
            # Update the quantity of the item in the bag
            bag[item_id] = quantity
            messages.success(request, f'The quantity of {tour.name} has been updated to {quantity}.')
        else:
            # Remove the item if the quantity is 0 or less
            if str(item_id) in bag:
                bag.pop(str(item_id))
                messages.success(request, f'{tour.name} has been removed from your travel backpack.')
            else:
                messages.error(request, f'{tour.name} was not found in your backpack.')

        # Update the session bag
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    except TourProducts.DoesNotExist:
        messages.error(request, "Tour not found.")
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('view_bag')

def remove_from_backpack(request, item_id):
    """Remove the tour product from the backpack."""
    try:
        bag = request.session.get('bag', {})

        if str(item_id) in bag:
            # Remove the item from the bag
            tour = TourProducts.objects.get(pk=item_id)
            bag.pop(str(item_id))
            messages.success(request, f'Tour {tour.name} successfully removed from your travel backpack!')
            request.session['bag'] = bag  # Update the session bag
        else:
            messages.error(request, 'Tour not found in the backpack.')
        
        print(f"Received item_id: {item_id}") 

        return redirect(reverse('view_bag'))

    except TourProducts.DoesNotExist:
        messages.error(request, "Tour not found.")
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('view_bag')
