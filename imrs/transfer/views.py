from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaterialTransfer, MaterialTransferItems
from .models import Item
from project_site.models import Inventory
from inventory.views import InventoryListView
from .forms import TransferModelForm
from django.contrib import messages
from django.views import generic
from django.db.models import Prefetch


# Create your views here.


# class TransferListView(LoginRequiredMixin, generic.ListView):
#     template_name = "transfer/transfer.html"
#     context_object_name = "transfer"
#     model = MaterialTransfer

#     def get_queryset(self):
#         qs = MaterialTransfer.objects.all()
#         return qs


# class TransferAddView(LoginRequiredMixin, generic.CreateView):
#     template_name = "transfer/transfer_add.html"
#     form_class = TransferModelForm
#     model = MaterialTransfer

#     def get_success_url(self):
#         return reverse("transfer:list-transfer")

#     def form_valid(self, form):
#         # Save the validated data of your object
#         self.object = form.save(commit = False)
#         # Update the value of the desired field
#         self.object.site = self.request.user.site
#         # Save the object to commit the changes
#         self.object.save()
#         return super(TransferAddView, self).form_valid(form)

#     def get_queryset(self):
#         user = self.request.user
#         return MaterialTransfer.objects.all()


# class TransferUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
#     template_name = "transfer/transfer_update.html"
#     form_class = TransferModelForm

#     def get_queryset(self):
#         user = self.request.user
#         return MaterialTransfer.objects.all()

#     def get_success_url(self):
#         return reverse("transfer:list-transfer")

#     def form_valid(self, form):
#         form.save()
#         messages.info(self.request, "Transfer details have been updated")
#         return super(TransferUpdateView, self).form_valid(form)


# class TransferDetailView(LoginRequiredMixin, generic.DetailView): #for main office
#     model = MaterialTransfer
#     template_name = "transfer/transfer_detail.html"
#     context_object_name = "transfer"
#     queryset = MaterialTransfer.objects.prefetch_related(
#         Prefetch('materialtransferitems_set', MaterialTransferItems.objects.select_related('item'))
#     )

#     def get_success_url(self):
#         return reverse("transfer:detail-transfer")