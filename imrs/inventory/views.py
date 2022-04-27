from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from project_site.models import Inventory
from .forms import *
from django.contrib import messages
from project_site.models import Site
from .filters import InventoryFilter
import json


# class InventoryDispatchListView(generic.ListView):
#     def dispatch(self, request, *args, **kwargs):
        

class InventoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "inventory/inventory.html"
    context_object_name = "data"
    model = Inventory
    sites_list = SiteModelForm()

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['sites_list'] = self.sites_list
    #     context['selected_site'] = self.selected_site

    def get_queryset(self):
        if self.request.user.role <= 1: 
            if self.request.GET.get('sites'):
                selected_site = self.request.GET.get('sites')
                qs = {
                    'selected_site': Site.objects.get(site=selected_site),
                    "selected_inventory": Inventory.objects.filter(site=selected_site),
                }
            else:
                qs = {}
            qs.update({'sites_list': self.sites_list})
        else:
            qs = {
                "selected_inventory": Inventory.objects.filter(site__site=self.request.user.site.site),
            }
        return qs
        


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

