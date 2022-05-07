from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from project_site.models import Inventory
from .forms import *
from project_site.models import Site


class InventoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "inventory/inventory.html"
    context_object_name = "data"
    model = Inventory
    sites_list = SiteModelForm()

    def get_queryset(self):
        if self.request.user.role <= 2: 
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
    model = Inventory
    
    def get_success_url(self):
        return reverse_lazy("inventory:detail-inventory", args=[self.object.pk])
    
    def form_valid(self,form):
        form.save()
        return super(InventoryUpdateView, self).form_valid(form)

class InventoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Inventory
    template_name = "inventory/inventory_detail.html"
    def get_success_url(self):
        return reverse_lazy("inventory:detail-inventory")


class InventoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Inventory

    def get_success_url(self):
        return reverse_lazy("inventory:list-inventory")


class InventoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Inventory

    def get_success_url(self):
        return reverse_lazy("inventory:list-inventory")

