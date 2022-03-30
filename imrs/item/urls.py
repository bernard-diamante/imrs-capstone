from django.urls import path
from .views import *

app_name = 'item'

urlpatterns = [
    # item
    path('', ItemListView.as_view(), name='list-item'),
    path('add/', ItemAddView.as_view(), name='add-item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update-item'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail-item'),
    
    # path('add-item-inv/<int:pk>', ItemAddInvView.as_view(), name='add-item-inv'),
    path('cart/', CartListView.as_view(), name='item-cart'),
    # path('cart/<int:pk>/add/', add_to_cart, name='add-to-cart'),
    
    path('cart/add/', addCartItem, name='add-cart'),
    path('cart/<int:item>/delete', deleteCartItem, name='delete-cart'),
]
