from django.shortcuts import get_object_or_404
from tour_products.models import TourProducts


def travelbag_contents(request):
    travel_backpack = []
    total = 0
    tour_count = 0
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        try:
            tour = get_object_or_404(TourProducts, pk=item_id)
            total += quantity * tour.price
            tour_count += quantity
            travel_backpack.append({
                'item_id': item_id,
                'quantity': quantity,
                'tour': tour,
            })
        except TourProducts.DoesNotExist:
            print(f"Error: Tour with id {item_id} does not exist.")
            continue

    grand_total = total + tour_count

    context = {
        'travel_backpack': travel_backpack,
        'total': total,
        'tour_count': tour_count,
        'grand_total': grand_total,
    }

    return context
