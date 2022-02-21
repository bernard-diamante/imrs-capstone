from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

app_name = 'inventory'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('', AddItemView.as_view(), name='add-item'),
    path('', UpdateItemView.as_view(), name='update-item'),
    path('', ItemDetailView.as_view(), name='item-detail'),
    path('requisition/', RequisitionListView.as_view(), name='requisition-list'),
    path('', AddRequisitionView.as_view(), name='add-requisition'),
    path('', UpdateRequisitionView.as_view(), name='update-requisition'),
    path('', DeleteRequisitionView.as_view(), name='delete-requisition'),
    # path('transfer/', TransferListView.as_view(), name='transfer-list'),
    # path('', AddTransferView.as_view(), name='add-transfer'),
    # path('', UpdateTransferView.as_view(), name='update-transfer'),
    # path('', DeleteTransferView.as_view(), name='delete-transfer'),
    path('projectsite/', ListSiteView.as_view(), name='site-list'),
    path('', CreateSiteView.as_view(), name='add-site'),
    path('', UpdateSiteView.as_view(), name='update-site'),
    path('', DeleteSiteView.as_view(), name='delete-site'),
]
