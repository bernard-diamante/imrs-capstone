from django.urls import path
from .views import *


app_name = 'inventory'

urlpatterns = [
    # inventory
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('<int:pk>/update/', InventoryUpdateView.as_view(), name='update-inv-item'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='detail-inv-item'),
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='delete-inv-item'),
]
