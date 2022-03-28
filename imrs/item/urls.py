from django.urls import path
from .views import *

app_name = 'item'

urlpatterns = [
    # item
    path('', ItemListView.as_view(), name='item-list'),
    path('add/', ItemAddView.as_view(), name='add-item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    # path('add-item-inv/<int:pk>', ItemAddInvView.as_view(), name='add-item-inv'),
    path('cart/', CartListView.as_view(), name='item-cart'),
    # path('cart/<int:pk>/add/', add_to_cart, name='add-to-cart'),

    path('cart/update_item/', updateItem, name='update_item'),
]
