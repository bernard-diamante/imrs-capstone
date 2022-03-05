from django.urls import path
from .views import *

app_name = 'project_site'

urlpatterns = [
    # project_site
    path('', SiteListView.as_view(), name='site-list'),
    path('add/', SiteCreateView.as_view(), name='add-site'),
    path('<int:pk>/update/', SiteUpdateView.as_view(), name='update-site'),
    path('<int:pk>/delete/', SiteDeleteView.as_view(), name='delete-site'),
]