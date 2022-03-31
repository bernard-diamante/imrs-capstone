from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import AddItemModelForm, UpdateItemModelForm
from .models import Item
from project_site.models import *
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from project_site.models import Cart
import json
from django.http import HttpResponseRedirect

# from inventory.views import InventoryCreateView

# Create your views here.
class ItemListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item.html"
    context_object_name = "data"

    def get_queryset(self):
        items = Item.objects.all()
        cart = Cart.objects.all()
        
        inventory = Inventory.objects.all().values_list()
        cart_values = Cart.objects.all().values_list()

        itemID_list = []
        cartItemID_list = []

        for i in inventory:
            itemID_list.append(i[0])
        for i in cart_values:
            cartItemID_list.append(i[0])

        qs = { 
            "items": items,
            "itemID_list": itemID_list,
            "cartItemID_list": cartItemID_list,
            "cart": cart
            }
        return qs
        

# class AddItemInvView(generic.CreateView):
#     form_class = AddItemForm
#     def get_success_url(self):
#         return reverse_lazy("item-list")

#     def form_valid(self, form):
#         return super(AddItemInvView, self).form_valid(form)


class ItemAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "item/item_add.html"
    form_class = AddItemModelForm
    
    def get_success_url(self):
        return reverse_lazy("item:list-item")

    def form_valid(self, form):
        return super(ItemAddView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "item/item_update.html"
    form_class = UpdateItemModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Item.objects.all()

    def get_success_url(self):
        return reverse_lazy("item:list-item")
    
    def form_valid(self, form):
        form.save()
        return super(ItemUpdateView, self).form_valid(form)

class ItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "item/item_delete.html"

    def get_success_url(self):
        return reverse_lazy("item:list-item")

    def get_queryset(self):
        user = self.request.user
        return Item.objects.all()

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "item/item_detail.html"
    model = Item

    def get_success_url(self):
        return reverse_lazy("item:detail-item")


# Cart Functions
class CartListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item_summary.html"
    context_object_name = "cart"

    def get_queryset(self):
        qs = Cart.objects.all()
        return qs

def user_check(user):
    return user.username


@user_passes_test(user_check) 
def addCartItem(request):
    data = json.loads(request.body)
    itemID = data['item']
    action = data['action']

    item = Item.objects.get(item=item)
    
    cartItem = Item.objects.get(item=item)
    cart,created = Cart.objects.get_or_create(site=request.user.site, cartItem=cartItem)
    cart.save()
    return JsonResponse('Item was added', safe=False)


def deleteCartItem(request, item):
    item = Item.objects.get(pk=item)
    # cartItem = Item.objects.get(pk=item)
    cart = Cart.objects.filter(site=request.user.site.site, cartItem=item.item)
    cart.delete()
    return HttpResponseRedirect(reverse_lazy('item:item-cart'))
    

    # item = Item.objects.filter(id=kwargs.get('item', "")).first()
    # cartItems = Site.objects.get_or_create(cartItem=item)
    # if len(cartItems) == 0:
    #     # TODO: Show cart is empty
    #     pass
    # else:
    #     pass

    #     # for item in cartItems: