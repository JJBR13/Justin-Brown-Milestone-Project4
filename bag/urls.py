from django.urls import path
from . import views
from .views import update_backpack

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_to_backpack, name='add-to-backpack'),
    path('update/<item_id>/', views.update_backpack, name='update_backpack'),
]
