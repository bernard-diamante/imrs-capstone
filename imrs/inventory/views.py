from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages


class DashboardListView(generic.ListView):
    template_name = "html file"

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)

        user = self.request.user

        # Add dashboard contents

        return context

class InventoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "inventory.html"
    def get_queryset(self):
        queryset = Site_Item_Inventory.objects.all()
    context_object_name = "inventory"

    def get_context_data(self, **kwargs):
        context = super(InventoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        
        #Conditionals

        return context
        

class ItemListView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    context_object_name = "item"

    def get_queryset(self):
        queryset = Item.objects.all()

class ItemAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "html file"
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
        messages.info(self.request, "Messages")
        return super(ItemUpdateView, self).form_valid(form)

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "html file"
    context_object_name = "item"

    def get_queryset(self):
        return Item.objects.all()

class RequisitionListView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    queryset = Material_Requisition.objects.all()
    context_object_name = "requisition"

    def get_queryset(self):
        queryset = Site_Item_Inventory.objects.all()
    context_object_name = "inventory"

    def get_context_data(self, **kwargs):
        context = super(InventoryListView, self).get_context_data(self, **kwargs)
        user = self.request.user
        
        return context

class RequisitionAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "html file"
    form_class = RequisitionModelForm

    def get_success_url(self):
        return reverse("requisition-list")

    def form_valid(self, form):
        return super(RequisitionAddView, self).form_valid(form)

class RequisitionUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "html file"
    form_class = RequisitionModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Material_Requisition.objects.all()

    def get_success_url(self):
        return reverse("requisition-list")
    
    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Messages")
        return super(RequisitionUpdateView, self).form_valid(form)

class RequisitionDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "url"

    def get_success_url(self):
        return reverse("requisition-list")

    def get_queryset(self):
        user = self.request.user
        return Material_Requisition.objects.all()

class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'html file'
    form_class = SiteModelForm

    def get_success_url(self):
        return reverse("site-list")

    def form_valid(self, form):
        return super(SiteCreateView, self).form_valid(form)

class SiteListView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    context_object_name = "site"

    def get_queryset(self):
        queryset = Site_Item_Inventory.objects.all()

class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'html file'
    form_class = SiteModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()

    def get_success_url(self):
        return reverse("site-list")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Messages")
        return super(SiteUpdateView, self).form_valid(form)

class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "html file"

    def get_success_url(self):
        return reverse("site-list")

    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()