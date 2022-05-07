from django.urls import path, include
from .views import *

app_name = 'item'

urlpatterns = [
    path('', ItemListView.as_view(), name='list-item'),
    path('add/', ItemAddView.as_view(), name='add-item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update-item'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail-item'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='delete-item'),
    path('cart/', CartListView.as_view(), name='list-cart'),
    path('cart/add/', addCartItem, name='add-cart'),
    path('cart/<int:item>/delete', deleteCartItem, name='delete-cart'),
    path("select2/", include("django_select2.urls")),
    path('cart/submit/', sendCart, name='send-cart'),
]
