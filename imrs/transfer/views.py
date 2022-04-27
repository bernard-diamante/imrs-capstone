from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaterialTransfer, MaterialTransferItems
from .models import Item
from project_site.models import Inventory
from inventory.views import InventoryListView
from .forms import *
from django.contrib import messages
from django.views import generic
from django.db.models import Prefetch
from django.urls import reverse_lazy


class TransferListView(LoginRequiredMixin, generic.ListView):
    template_name = "transfer/transfer.html"
    context_object_name = "transfer"
    
    def get_queryset(self):
        if self.request.user.role >= 2:
            qs = {
                'transfers': MaterialTransfer.objects.filter(site=self.request.user.site)
            }
        else:
            qs = {
                'transfers': MaterialTransfer.objects.all()
            }
        return qs


class TransferAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "transfer/transfer_add.html"
    form_class = TransferModelForm
    model = MaterialTransfer

    def get_success_url(self):
        return reverse("transfer:list-transfer")
    
    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     print(form.errors)
    #     return response

    def form_valid(self, form, **kwargs):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        # form.instance.site = MaterialTransfer.objects.get(site=ctx['req'].site)
        # print(form.instance.site)
        form.instance.requisition = ctx['req']
        if inlines.is_valid() and form.is_valid():
            # req = form.save(commit = False)
            # req.site = self.request.user.site
            tran = form.save()
            inlines.instance = tran
            inlines.save()
        
    
        return super(TransferAddView, self).form_valid(form)
    
    

    def get_context_data(self, **kwargs):
        ctx=super(TransferAddView,self).get_context_data(**kwargs)
        ctx['req'] = MaterialRequisition.objects.get(pk=self.kwargs['req'])
        if self.request.method == 'POST':
            # ctx['form']=TransferModelForm(self.request.POST, request=self.request)
            # ctx['inlines']=TransferInlineFormSet(self.request.POST, request=self.request)
            ctx['form']=TransferModelForm(self.request.POST)
            ctx['inlines']=TransferInlineFormSet(self.request.POST)
            ctx['form'].fields['transferStatus'].initial = 0
        else:
            # ctx['form']=TransferModelForm(request=self.request)
            # ctx['form']=TransferModelForm(initial={'requisition': ctx['req']})
            ctx['form']=TransferModelForm()
            ctx['form'].fields['transferStatus'].initial = 0
            ctx['inlines']=TransferInlineFormSet(form_kwargs={'req':ctx['req'].pk})
        return ctx

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super().get_form_kwargs(*args, **kwargs)
    #     # kwargs['req'] = MaterialRequisition.objects.get(pk=self.kwargs.get("req"))
    #     kwargs['req'] = self.kwargs.get("req")
    #     # ctx['req'].pk
    #     return kwargs

class TransferUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
    template_name = "transfer/transfer_update.html"
    form_class = TransferModelForm
    model = MaterialTransfer

    def get_success_url(self):
        return reverse("transfer:list-transfer")

    # def form_valid(self, form):
    #     form.save()
    #     messages.info(self.request, "Transfer details have been updated")
    #     return super(TransferUpdateView, self).form_valid(form)

    def form_valid(self, form, **kwargs):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        # form.instance.site = MaterialTransfer.objects.get(site=ctx['req'].site)
        # print(form.instance.site)
        if inlines.is_valid() and form.is_valid():
            # req = form.save(commit = False)
            # req.site = self.request.user.site
            tran = form.save()
            inlines.instance = tran
            inlines.save()
        return super(TransferUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx=super(TransferUpdateView,self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            # ctx['form']=TransferModelForm(self.request.POST, request=self.request)
            # ctx['inlines']=TransferInlineFormSet(self.request.POST, request=self.request)
            ctx['form']=TransferModelForm(self.request.POST)
            ctx['inlines']=TransferInlineUpdateFormSet(self.request.POST)
            ctx['form'].fields['transferStatus'].initial = 0
        else:
            # ctx['form']=TransferModelForm(request=self.request)
            # ctx['form']=TransferModelForm(initial={'requisition': ctx['req']})
            ctx['form']=TransferModelForm(instance=self.object)
            ctx['form'].fields['transferStatus'].initial = 0
            ctx['inlines']=TransferInlineUpdateFormSet(instance=self.object)
        return ctx


class TransferDetailView(LoginRequiredMixin, generic.DetailView): #for main office
    model = MaterialTransfer
    template_name = "transfer/transfer_detail.html"
    context_object_name = "transfer"
    queryset = MaterialTransfer.objects.prefetch_related(
        Prefetch('materialtransferitems_set', MaterialTransferItems.objects.select_related('item'))
    )

    def get_success_url(self):
        return reverse("transfer:detail-transfer")

class TransferDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MaterialTransfer
    def get_success_url(self):
        return reverse_lazy("transfer:list-transfer")