from django.shortcuts import render
from tour_products.models import TourProducts


def index(request):
    ''' Return homepage '''

    tourproducts = TourProducts.objects.all().order_by('?')
    
    context = {
        'tourproducts': tourproducts
    }

    return render(request, 'home/index.html', context)
