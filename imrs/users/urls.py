from django.urls import path
from django.contrib.auth.views import SignupView
from .views import *

app_name = 'users'

urlpatterns = [
    # users
    path('', UserListView.as_view(), name='list-user'),
    path('add/', SignupView.as_view(), name='add-user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update-user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
]