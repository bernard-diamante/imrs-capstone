from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from project_site.models import Inventory
from .forms import *
from django.contrib import messages


class InventoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "inventory/inventory.html"
    context_object_name = "inventory"
    model = Inventory
    def get_queryset(self):
        qs = Inventory.objects.all()
        return qs
        
        #Conditionals

class InventoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'inventory/inventory_update.html'
    form_class = SiteItemInventoryModelForm

    def get_queryset(self):
        user = self.request.user
        return Inventory.objects.all()
    
    def get_success_url(self):
        return reverse("inventory:detail-inventory", args=[self.object.pk])
    
    def form_valid(self,form):
        form.save()
        messages.info(self.request, "Inventory has been updated")
        return super(InventoryUpdateView, self).form_valid(form)

class InventoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Inventory
    template_name = "inventory/inventory_detail.html"
    def get_success_url(self):
        return reverse("inventory:detail-inventory")


class InventoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Inventory

    def get_success_url(self):
        return reverse("inventory:list-inventory")

    def get_queryset(self):
        user = self.request.user
        return Inventory.objects.all()

class InventoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Inventory

    def get_success_url(self):
        return reverse("inventory:list-inventory")

    def get_queryset(self):
        user = self.request.user
        return Inventory.objects.all()

