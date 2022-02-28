from django.urls import path
from .views import *


app_name = 'inventory'

urlpatterns = [
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('', InventoryListView.as_view(), name='inventory-list'),

    # Item
    path('item/', ItemListView.as_view(), name='item-list'),
    path('item/add/', ItemAddView.as_view(), name='add-item'),
    path('item/update/<int:pk>/', ItemUpdateView.as_view(), name='update-item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),

    # Site Inventory
    path('', .as_view(), name=''),
    path('', .as_view(), name=''),
    path('', .as_view(), name=''),
    path('', .as_view(), name=''),
    path('', .as_view(), name=''),

    # Requisition
    
    path('requisition/', RequisitionListView.as_view(), name='requisition-list'),
    path('requisition/add/', RequisitionAddView.as_view(), name='add-requisition'),
    path('requisition/update/<int:pk>/', RequisitionUpdateView.as_view(), name='update-requisition'),
    path('requisition/delete/<int:pk>/', RequisitionDeleteView.as_view(), name='delete-requisition'),

    # Site management
    path('site/', SiteListView.as_view(), name='site-list'),
    path('site/add/', SiteCreateView.as_view(), name='add-site'),
    path('site/update/<int:pk>/', SiteUpdateView.as_view(), name='update-site'),
    path('site/delete/<int:pk>/', SiteDeleteView.as_view(), name='delete-site'),
]
