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

    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        
        if inlines.is_valid() and form.is_valid():
            # req = form.save(commit = False)
            form.instance.site = self.request.user.site
            # req.site = self.request.user.site
            tran = form.save()
            inlines.instance = tran
            inlines.save()

    def get_context_data(self, **kwargs):
        ctx=super(TransferAddView,self).get_context_data(**kwargs)
        ctx['item_list'] = TranItemModelForm()
        if self.request.method == 'POST':
            ctx['form']=TransferModelForm(self.request.POST)
            ctx['inlines']=TransferInlineFormSet(self.request.POST)
        else:
            ctx['form']=TransferModelForm()
            ctx['inlines']=TransferInlineFormSet()
        return ctx

    def get_initial(self):
        initial = super(TransferAddView, self).get_initial()
        initial["site"] = self.request.user.site
        return initial


class TransferUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
    template_name = "transfer/transfer_update.html"
    form_class = TransferModelForm
    model = MaterialTransfer

    def get_success_url(self):
        return reverse("transfer:list-transfer")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Transfer details have been updated")
        return super(TransferUpdateView, self).form_valid(form)


class TransferDetailView(LoginRequiredMixin, generic.DetailView): #for main office
    model = MaterialTransfer
    template_name = "transfer/transfer_detail.html"
    context_object_name = "transfer"
    queryset = MaterialTransfer.objects.prefetch_related(
        Prefetch('materialtransferitems_set', MaterialTransferItems.objects.select_related('item'))
    )

    def get_success_url(self):
        return reverse("transfer:detail-transfer")