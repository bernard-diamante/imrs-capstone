from django.urls import path
from .views import *



app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='list-inventory'),
    path('<str:pk>/update/', InventoryUpdateView.as_view(), name='update-inventory'),
    path('<str:pk>/', InventoryDetailView.as_view(), name='detail-inventory'),
    path('add/', InventoryCreateView.as_view(), name='add-inventory'), # TEST
    path('<str:pk>/delete/', InventoryDeleteView.as_view(), name='delete-inventory'),
]
