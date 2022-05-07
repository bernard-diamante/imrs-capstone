from django.urls import path
from .views import *

app_name = 'requisition'

urlpatterns = [
    path('', RequisitionListView.as_view(), name='list-requisition'),
    path('add/', RequisitionAddView.as_view(), name='add-requisition'),
    path('<int:pk>/update/', RequisitionUpdateView.as_view(), name='update-requisition'),
    path('<int:pk>/', RequisitionDetailView.as_view(), name='detail-requisition'),
]
