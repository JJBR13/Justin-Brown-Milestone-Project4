from django.urls import path
from . import views

urlpatterns = [
    path('<tour_id>', views.tour_breakdown, name="tour-breakdown"),
]