from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
]