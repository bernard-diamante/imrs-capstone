from django.shortcuts import reverse, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Material_Requisition
from project_site.models import Inventory
from inventory.views import InventoryListView
from .forms import RequisitionModelForm
from django.contrib import messages
from django.views import generic

# Create your views here.


class RequisitionListView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    queryset = Material_Requisition.objects.all()
    context_object_name = "requisition"

    def get_queryset(self):
        queryset = Inventory.objects.all()
    context_object_name = "inventory"

    def get_context_data(self, **kwargs):
        context = super(InventoryListView, self).get_context_data(
            self, **kwargs)
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
        messages.info(self.request, "Requisition details have been updated")
        return super(RequisitionUpdateView, self).form_valid(form)


class RequisitionDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "url"

    def get_success_url(self):
        return reverse("requisition-list")

    def get_queryset(self):
        user = self.request.user
        return Material_Requisition.objects.all()
