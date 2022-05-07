from django.urls import path
from .views import *

app_name = 'transfer'

urlpatterns = [
    path('', TransferListView.as_view(), name='list-transfer'),
    path('<int:req>/add/', TransferAddView.as_view(), name='add-transfer'),
    path('<int:pk>/update/', TransferUpdateView.as_view(), name='update-transfer'),
    path('<int:pk>/', TransferDetailView.as_view(), name='detail-transfer'),
    path('<int:pk>/change_status', updateTransferStatus, name='status-transfer'),
    path('<int:pk>/delete/', TransferDeleteView.as_view(), name='delete-transfer'),
]
