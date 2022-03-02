from django.urls import path
from .views import *

app_name = 'item'

urlpatterns = [
    # item
    path('', ItemListView.as_view(), name='item-list'),
    path('add/', ItemAddView.as_view(), name='add-item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update-item'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
