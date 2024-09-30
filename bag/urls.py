from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_to_backpack, name='add-to-backpack'),
    path('update/<item_id>/', views.update_backpack, name='update_backpack'),

    path('remove/<int:item_id>/', views.remove_from_backpack, name='remove_from_backpack'),
]
