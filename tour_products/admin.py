from django.contrib import admin
from .models import TourProducts

class TourProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'four_facts',
        'date_available',
        'image', 
    )

admin.site.register(TourProducts)


