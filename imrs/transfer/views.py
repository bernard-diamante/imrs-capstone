from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaterialTransfer, MaterialTransferItems
from .forms import TransferModelForm, TransferInlineFormSet
from django.views import generic
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.shortcuts import render
from requisition.models import MaterialRequisition, MaterialRequisitionItems
from item.models import Item
from django.http import HttpResponseRedirect
import datetime
from project_site.models import Inventory

class TransferListView(LoginRequiredMixin, generic.ListView):
    template_name = "transfer/transfer.html"
    context_object_name = "transfers"
    model = MaterialTransfer
    
    def get_queryset(self):
        if self.request.user.role >= 2:
            qs = {
                'incomingTransfers': MaterialTransfer.objects.filter(requisition__site=self.request.user.site.site),
                'outgoingTransfers': MaterialTransfer.objects.filter(site__site=self.request.user.site.site),
            }
            print(qs)
        else:
            qs = {
                'transfers': MaterialTransfer.objects.all(),
            }
        return qs


class TransferAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "transfer/transfer_add.html"
    form_class = TransferModelForm
    model = MaterialTransfer

    def get_success_url(self):
        return reverse_lazy("transfer:list-transfer")

    def form_valid(self, form, **kwargs):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        form.instance.requisition = ctx['req']
        if inlines.is_valid() and form.is_valid():
            tran = form.save()
            inlines.instance = tran
            inlines.save()
        return super(TransferAddView, self).form_valid(form)
    
    

    def get_context_data(self, **kwargs):
        ctx=super(TransferAddView,self).get_context_data(**kwargs)
        ctx['req'] = MaterialRequisition.objects.get(pk=self.kwargs['req'])
        req = list(MaterialRequisitionItems.objects.filter(requisition=ctx['req']).values_list('item', flat=True))
        ctx['item'] = Item.objects.filter(item__in=req)
        if self.request.method == 'POST':
            ctx['form']=TransferModelForm(self.request.POST)
            ctx['inlines']=TransferInlineFormSet(self.request.POST, form_kwargs={'reqs': list(MaterialRequisitionItems.objects.filter(requisition=ctx['req'].pk).values_list('item', flat=True))})
            ctx['form'].fields['transferStatus'].initial = 0
        else:
            ctx['form']=TransferModelForm()
            ctx['form'].fields['transferStatus'].initial = 0
            ctx['inlines']=TransferInlineFormSet(form_kwargs={'reqs': list(MaterialRequisitionItems.objects.filter(requisition=ctx['req'].pk).values_list('item', flat=True))})
        return ctx




class TransferUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
    template_name = "transfer/transfer_update.html"
    form_class = TransferModelForm
    model = MaterialTransfer

    def get_success_url(self):
        return reverse_lazy("transfer:list-transfer")

    def form_valid(self, form, **kwargs):
        ctx = self.get_context_data()
        if form.is_valid():
            form.save()
        return super(TransferUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx=super(TransferUpdateView,self).get_context_data(**kwargs)
        if self.request.user.role >= 2:
            if self.request.method == 'POST':
                ctx['form']=EngineerTransferModelForm(self.request.POST)
            else:
                ctx['form']=EngineerTransferModelForm(instance=self.object)

        else:
            if self.request.method == 'POST':
                ctx['form']=TransferModelForm(self.request.POST)
                ctx['form'].fields['transferStatus'].initial = 0
            else:
                ctx['form']=TransferModelForm(instance=self.object)
                ctx['form'].fields['transferStatus'].initial = 0
        return ctx


class TransferDetailView(LoginRequiredMixin, generic.DetailView): #for main office
    model = MaterialTransfer
    template_name = "transfer/transfer_detail.html"
    context_object_name = "transfer"
    queryset = MaterialTransfer.objects.prefetch_related(
        Prefetch('materialtransferitems_set', MaterialTransferItems.objects.select_related('item'))
    )

    def get_success_url(self):
        return reverse_lazy("transfer:detail-transfer")

class TransferDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MaterialTransfer
    def get_success_url(self):
        return reverse_lazy("transfer:list-transfer")


def updateTransferStatus(request, pk):
    transfer = MaterialTransfer.objects.filter(pk=pk)
    
    transferItems = MaterialTransferItems.objects.filter(
        transfer=pk
    )

    # Material Transfer has been approved
    if transfer[0].transferStatus == 0:
        transfer.update(
        transferStatus = 1,
        transferDateModified = datetime.datetime.now()
        )
        for item in transferItems:
            quantity = item.itemQuantity
            transferItem = item.item.item

            originSiteInventoryItems = Inventory.objects.filter(
                site=transfer[0].site.site,
                item__item = transferItem
                )
            originSiteInventoryItems.update(
                siteItemCount = originSiteInventoryItems[0].siteItemCount - quantity
                )

    # Material Transfer has been delivered
    elif transfer[0].transferStatus == 1:
        transfer.update(
        transferStatus = 2,
        transferDateModified = datetime.datetime.now()
        )
        for item in transferItems:
            quantity = item.itemQuantity
            inventoryItem = item.item.item
            
            destinationInventoryItems = Inventory.objects.filter(
                site=transfer[0].requisition.site.site,
                item__item = inventoryItem
                )
            destinationInventoryItems.update(
                siteItemCount = destinationInventoryItems[0].siteItemCount + quantity
                )
            # index += 1 
    
    
    return HttpResponseRedirect(reverse_lazy('transfer:detail-transfer',
                                             kwargs={'pk': pk}))