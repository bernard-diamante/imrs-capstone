from django.urls import path
from .views import *
# from dashboard.views import DashboardListView


app_name = 'requisition'

urlpatterns = [
    # requisition
    path('', RequisitionListView.as_view(), name='list-requisition'),
    path('add/', RequisitionAddView.as_view(), name='add-requisition'),
    path('<int:pk>/update/', RequisitionUpdateView.as_view(), name='update-requisition'),
    # path('<int:pk>/delete/', RequisitionDeleteView.as_view(), name='delete-requisition'),
    path('<int:pk>/', RequisitionDetailView.as_view(), name='detail-requisition'),
]
