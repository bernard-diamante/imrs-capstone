from django.urls import path
from .views import *


app_name = 'inventory'

urlpatterns = [
    # inventory
    path('', InventoryListView.as_view(), name='list-inventory'),
    path('<int:pk>/update/', InventoryUpdateView.as_view(), name='update-inventory'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='detail-inventory'),
    path('add/', InventoryCreateView.as_view(), name='add-inventory'), # TEST
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='delete-inventory'),
]
