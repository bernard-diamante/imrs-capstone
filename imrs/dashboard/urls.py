from django.urls import path
from .views import *
from django.views.generic import TemplateView


app_name = 'dashboard'
urlpatterns = [
    path('', DashboardListView.as_view(), name='dashboard'),
    # path('', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
]