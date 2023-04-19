from django.shortcuts import render, get_object_or_404
from tour_products.models import TourProducts


def tour_breakdown(request, tour_id):
    ''' View that shows individual tour breakdown '''

    data = Model.objects.all()

    tour = get_object_or_404(TourProducts, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_breakdown.html', context)
