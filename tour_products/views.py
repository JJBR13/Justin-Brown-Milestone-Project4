from django.shortcuts import render
from .models import TourProducts


def all_tours(request):
    ''' A view that shows all tours '''

    tourproducts = TourProducts.objects.all()

    context = {
        'tourproducts': tourproducts,
    }

    return render(request, 'tourproducts/tour_products.html', context)
