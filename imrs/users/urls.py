from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    # users
    path('', UserListView.as_view(), name='list-user'),
    path('add/', UserCreateView.as_view(), name='add-user'),
    path('<str:pk>/update/', UserUpdateView.as_view(), name='update-user'),
    path('<str:pk>/delete/', UserDeleteView.as_view(), name='delete-user'),
    path('<str:pk>/', UserDetailView.as_view(), name='detail-user')
]