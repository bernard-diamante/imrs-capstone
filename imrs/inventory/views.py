from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.generic import (
    ListView, TemplateView, DetailView, 
    CreateView, UpdateView, DeleteView
    )
from .models import *


# 1 - Dashboard
# ListView ?
class DashboardListView(ListView):
    pass


# 3, 3.1 - Inventory
# ListView
class InventoryListView(ListView):
    # template_name = "html file"
    queryset = Site_Item_Inventory.objects.all()
    context_object_name = "inventory"

# 3.2, 3.3, 3.4 - Add Item
# CreateView
class AddItemView(CreateView):
    template_name = "html file"
    # form_class = *insertmodelformhere*
    
    # def get_success_url(self):
        # return reverse("url")

# 3.x - Update Item
# UpdateView
class UpdateItemView(UpdateView):
    template_name = "html file"
    # form_class = *insertmodelformhere*
    ###
    
    def get_success_url(self):
        # return reverse("url")
        pass
    
# 3.x - Item Details
# DetailView
class ItemDetailView(DetailView):
    pass

# 4 - Requisition
# ListView
class RequisitionListView(ListView):
    # template_name = "html file"
    queryset = Material_Requisition.objects.all()
    context_object_name = "requisition"


# 4.1. 4.2, 4.3 - Add Requisition
# CreateView
class AddRequisitionView(CreateView):
    # template_name = "html file"
    # form_class = "modelform"
    pass
    def get_success_url(self):
        # return reverse("url")
        pass


# 4.4 - Update Requisition
# UpdateView
class UpdateRequisitionView(UpdateView):
    pass


# 4.5 - Delete Requisition
# DeleteView
class DeleteRequisitionView(DeleteView):
    pass


# 5 - Transfer
# ListView
class TransferListView(ListView):
    # template_name = "html file"
    queryset = Material_Transfer.objects.all()
    context_object_name = "transfer"

# 5.1 - Add Transfer
# CreateView
class AddTransferView(CreateView):
    pass

# 5.2 - Update Transfer
# UpdateView 
class UpdateTransferView(UpdateView):
    pass

# 5.3 Delete Transfer 
# DeleteView
class DeleteTransferView(DeleteView):
    pass


# 6.1 - Create Site
# CreateView
class CreateSite(CreateView):
    pass


# 6.2 - List Site
# ListView
class ListSite(ListView):
    pass


# 6.3 - Update Site
# UpdateView
class UpdateSite(UpdateView):
    pass


# 6.4 - Delete Site
# DeleteView
class DeleteSite(DeleteView):
    pass


