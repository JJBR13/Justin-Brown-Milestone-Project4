from .models import TourProducts


def tour_products(request):
    tours = TourProducts.objects.all()
    return {'tours': tours}
