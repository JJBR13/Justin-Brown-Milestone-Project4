from django.shortcuts import render, get_object_or_404
from .models import TourProducts


def all_tours(request):
    ''' A view that shows all tours '''

    tourproducts = TourProducts.objects.all()

    context = {
        'tourproducts': tourproducts,
    }

    return render(request, 'all_tours/tour_products.html', context)


def tour_breakdown(request, tour_id):
    ''' View that shows individual tour breakdown '''

    tour = get_object_or_404(TourProducts, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'all_tours/tour_breakdown.html', context)
