from django.conf import settings

def travelbag_contents(request):

    travel_backpack = []
    total = 0
    tour_count = 0

    context = {
        'travel_backpack': travel_backpack,
        'total': total,
        'tour_count': tour_count,
    }

    return context
