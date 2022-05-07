from django.urls import path
from .views import *

app_name = 'project_site'

urlpatterns = [
    path('', SiteDispatchView.as_view(), name='list-site'),
    path('add/', SiteCreateView.as_view(), name='add-site'),
    path('<int:pk>/update/', SiteUpdateView.as_view(), name='update-site'),
    path('<int:pk>/', SiteDetailView.as_view(), name='detail-site'),
    path('<int:pk>/delete/', SiteDeleteView.as_view(), name='delete-site'),
]