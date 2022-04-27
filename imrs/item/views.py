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
        
        # items_in_cart = Cart.objects.filter()

        qs = { 
            "items": items,
            }

        # If site manager or warehouse manager:
        if self.request.user.role >= 2:
            cart = Cart.objects.filter(site=self.request.user.site)
            inventory = Inventory.objects.filter(site__site=self.request.user.site.site).values_list('item__item', flat=True)
            cartItemID_list = list(Item.objects.filter(cart__site=self.request.user.site).values_list('item', flat=True)) #Find the items stored in a site
            cartItemID_list = list(Item.objects.in_bulk(cartItemID_list).keys()) #Convert the list into a dictionary and extract the keys from the dictionary
            qs.update({"cart": cart, "inventory": inventory, "cartItemID_list": cartItemID_list})
        return qs
        


class ItemAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "item/item_add.html"
    form_class = AddItemModelForm
    
    def get_success_url(self):
        return reverse_lazy("item:list-item")

    # def form_valid(self, form):
    #     return super(ItemAddView, self).form_valid(form)


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
    model = Item
    def get_success_url(self):
        return reverse_lazy("item:list-item")

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "item/item_detail.html"
    model = Item

    def get_success_url(self):
        return reverse_lazy("item:detail-item")

# Cart Functions
def user_check(user):
    return user.username


@user_passes_test(user_check)
def addCartItem(request):
    data = json.loads(request.body)
    item = data['item']
    action = data['action']

    item = Item.objects.get(pk=item)
    
    cartItem = Item.objects.get(item=item.item)
    cart,created = Cart.objects.get_or_create(site=request.user.site, cartItem=cartItem)
    cart.save()
    return JsonResponse('Item was added', safe=False)


def deleteCartItem(request, item):
    cart = Cart.objects.get(pk=item)
    cart.delete()
    return HttpResponseRedirect(reverse_lazy('item:list-cart'))
    
def sendCart(request):
    cart = Cart.objects.filter(site=request.user.site)

    # item is an Cart item
    for item in cart:
        inv_item = Inventory.objects.create(
            site=request.user.site,
            # Item ID = Cart Item's Item ID
            item=item.cartItem,
            siteItemCount = item.cartItemCount
            )
        inv_item.save()
        item.delete()
    return HttpResponseRedirect(reverse_lazy('item:list-item'))

class CartListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item_summary.html"
    context_object_name = "cart"

    def get_queryset(self):
        qs = Cart.objects.filter(site=self.request.user.site)
        return qs

    # def post(self, request, *args, **kwargs):
    #     sendCart(request)
        
    # def get_success_url(self):
    #     return reverse_lazy("item:list-item")

        # cart = Cart.objects.filter(site=request.user.site)

        # for item in cart:
        #     inv_item = Inventory.objects.get_or_create(
        #         site=request.user.site,
        #         item__item=item.cartItem__item,
        #         siteItemCount = item.cartItemCount
        #         )
        #     inv_item.save()
    #     qs = Cart.objects.filter(site=self.request.user.site)
    #     for item in qs:
            

# class CartListView(LoginRequiredMixin, generic.CreateView):
#     template_name = "item/item_summary.html"
#     context_object_name = "cart"
#     model = Inventory
#     form_class = 

#     def get_queryset(self):
#         qs = {
#             "cart_items":Cart.objects.filter(site=self.request.user.site)
#         }
#         return qs

#     def form_valid(self, form):
