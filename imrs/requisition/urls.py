from django.urls import path
from .views import *
from dashboard.views import DashboardListView


app_name = 'requisition'

urlpatterns = [
    # requisition
    path('', RequisitionListView.as_view(), name='requisition-list'),
    path('add/', RequisitionAddView.as_view(), name='add-requisition'),
    path('<int:pk>/update/', RequisitionUpdateView.as_view(), name='update-requisition'),
    path('<int:pk>/delete/', RequisitionDeleteView.as_view(), name='delete-requisition'),
]
