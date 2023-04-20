from django.conf import settings
from django.shortcuts import get_object_or_404
from tour_products.models import TourProducts

def travelbag_contents(request):

    travel_backpack = []
    total = 0
    tour_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        tour = get_object_or_404(TourProducts, pk=item_id)
        total += quantity * tour.price 
        tour_count += quantity
        travel_backpack.append({
            'item_id': item_id,
            'quantity': quantity,
            'tour': tour,
        })

    context = {
        'travel_backpack': travel_backpack,
        'total': total,
        'tour_count': tour_count,
    }

    return context
