from django.shortcuts import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import ItemModelForm, AddItemForm
from inventory.models import Inventory, CartItem, InventoryCart
from .models import Item

from inventory.views import InventoryCreateView

# Create your views here.
class ItemListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item.html"
    context_object_name = "items"

    def get_queryset(self):
        qs = Item.objects.all()
        return qs
        

# class ItemAddInvView(generic.CreateView):
#     form_class = AddItemForm
#     def get_success_url(self):
#         return reverse("item-list")

#     def form_valid(self, form):
#         return super(ItemAddInvView, self).form_valid(form)


class ItemAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "item.html"
    form_class = ItemModelForm
    
    def get_success_url(self):
        return reverse("item-list")

    def form_valid(self, form):
        return super(ItemAddView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "html file"
    form_class = ItemModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Item.objects.all()

    def get_success_url(self):
        return reverse("item-list")
    
    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Item has been updated")
        return super(ItemUpdateView, self).form_valid(form)

class ItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "url"

    def get_success_url(self):
        return reverse("item-list")

    def get_queryset(self):
        user = self.request.user
        return Item.objects.all()

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "html file"
    context_object_name = "item"

    def get_queryset(self):
        return Item.objects.filter(pk=self.pk)


# Cart Functions
class CartListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item_summary.html"
    context_object_name = "cart"

    def get_queryset(self):
        qs = InventoryCart.objects.all()
        return qs

def add_to_cart(request, **kwargs):
    cartItems = CartItem.objects.filter(id=kwargs.get('itemID', "")).first()
    if len(cartItems) != 0:
        for item in cartItems:
            if item.is_Ordered == True:
                pass