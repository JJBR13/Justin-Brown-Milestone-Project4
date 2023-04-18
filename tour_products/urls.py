from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='all-tours'),
    path ('<tour_id>', views.tour_breakdown, name="tour-breakdown"),
]
