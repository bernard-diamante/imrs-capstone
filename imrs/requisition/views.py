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
    template_name = "requisition/requisition.html"
    context_object_name = "requisition"
    model = Material_Requisition

    def get_queryset(self):
        qs = Material_Requisition.objects.all()
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super(RequisitionListView, self).get_context_data(
    #         self, **kwargs)
    #     user = self.request.user

        return context


class RequisitionAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "requisition/requisition_add.html"
    form_class = RequisitionModelForm
    model = Material_Requisition

    def get_success_url(self):
        return reverse("requisition:requisition-list")

    def form_valid(self, form):
        form.save()
        return super(RequisitionAddView, self).form_valid(form)

    def get_queryset(self):
        user = self.request.user
        return Material_Requisition.objects.all()


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
    template_name = "html file"
    model = Material_Requisition

    def get_success_url(self):
        return reverse("requisition:requisition-list")

    def get_queryset(self):
        user = self.request.user
        return Material_Requisition.objects.all()
