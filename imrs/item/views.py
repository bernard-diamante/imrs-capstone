from django.shortcuts import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import ItemModelForm
from .models import Item
from project_site.models import *
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from project_site.models import Cart
import json

# from inventory.views import InventoryCreateView

# Create your views here.
class ItemListView(LoginRequiredMixin, generic.ListView):
    template_name = "item/item.html"
    context_object_name = "data"

    def get_queryset(self):
        items = Item.objects.all()
        inventory = Inventory.objects.all().values_list()
        itemID_list = []

        for i in inventory:
            itemID_list.append(i[0])

        qs = { 
            "items": items,
            "itemID_list": itemID_list,
            }
        return qs
        

# class AddItemInvView(generic.CreateView):
#     form_class = AddItemForm
#     def get_success_url(self):
#         return reverse("item-list")

#     def form_valid(self, form):
#         return super(AddItemInvView, self).form_valid(form)


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
        qs = Site.objects.all()
        return qs

def user_check(user):
    return user.username


@user_passes_test(user_check) 
def updateItem(request):
    data = json.loads(request.body)
    itemID = data['itemID']
    action = data['action']

    print('Action: ',action)
    print('itemID: ',itemID)

    item = Item.objects.get(itemID=itemID)
    
    cartItem = Item.objects.get(itemID=itemID)
    cart,created = Cart.objects.get_or_create(siteID=request.user.site, cartItemID=cartItem)
    cart.save()
    return JsonResponse('Item was added', safe=False)


    # item = Item.objects.filter(id=kwargs.get('itemID', "")).first()
    # cartItems = Site.objects.get_or_create(cartItemID=item)
    # if len(cartItems) == 0:
    #     # TODO: Show cart is empty
    #     pass
    # else:
    #     pass

    #     # for item in cartItems: