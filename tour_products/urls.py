from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='all-tours'),
    path('<int:tour_id>', views.tour_breakdown, name="tour-breakdown"),
    path('add/', views.add_tour, name="add_tour"),
    path('edit/<int:tour_id>/', views.edit_tour, name="edit_tour"),
    
]
