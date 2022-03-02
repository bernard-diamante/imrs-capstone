from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages


class InventoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "inventory/inventory.html"
    context_object_name = "inventory"
    model = Site_Item_Inventory
    def get_queryset(self):
        qs = Site_Item_Inventory.objects.all()
        return qs
        
        #Conditionals

class InventoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'inventory/inventory_update.html'
    form_class = SiteItemInventoryModelForm

    def get_queryset(self):
        user = self.request.user
        return Site_Item_Inventory.objects.all()
    
    def get_success_url(self):
        return reverse("inventory:detail-inv-item", args=[self.object.pk])
    
    def form_valid(self,form):
        form.save()
        messages.info(self.request, "Messages")
        return super(InventoryUpdateView, self).form_valid(form)

class InventoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Site_Item_Inventory
    template_name = "inventory/inventory_detail.html"
    def get_success_url(self):
        return reverse("inventory:detail-inv-item")


class InventoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Site_Item_Inventory

    def get_success_url(self):
        return reverse("inventory:inventory-list")

    def get_queryset(self):
        user = self.request.user
        return Site_Item_Inventory.objects.all()