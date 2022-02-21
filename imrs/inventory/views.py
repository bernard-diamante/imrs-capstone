from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import *
from .forms import *

# 1 - Dashboard
# ListView ?
class DashboardListView(generic.ListView):
    pass

# --------------------------------------------------------------- #

# 3, 3.1 - Inventory
# ListView
class InventoryListView(LoginRequiredMixin, generic.ListView):
    # template_name = "html file"
    def get_queryset(self):
        queryset = Site_Item_Inventory.objects.all()
    context_object_name = "inventory"

# 3.2, 3.3, 3.4 - Add Item
# CreateView
class AddItemView(LoginRequiredMixin, generic.CreateView):
    template_name = "html file"
    form_class = ItemModelForm
    
    def get_success_url(self):
        # return reverse("url")
        pass

# 3.x - Update Item
# UpdateView
class UpdateItemView(LoginRequiredMixin, generic.UpdateView):
    template_name = "html file"
    form_class = ItemModelForm
    
    def get_success_url(self):
        # return reverse("url")
        pass
    
# 3.x - Item Details
# DetailView
class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "html file"
    context_object_name = "item"

    def get_queryset(self):
        # return Items.object.all()
        pass

# --------------------------------------------------------------- #

# 4 - Requisition
# ListView
class RequisitionListView(LoginRequiredMixin, generic.ListView):
    # template_name = "html file"
    queryset = Material_Requisition.objects.all()
    context_object_name = "requisition"


# 4.1. 4.2, 4.3 - Add Requisition
# CreateView
class AddRequisitionView(LoginRequiredMixin, generic.CreateView):
    # template_name = "html file"
    form_class = RequisitionModelForm
    pass
    def get_success_url(self):
        # return reverse("url")
        pass


# 4.4 - Update Requisition
# UpdateView
class UpdateRequisitionView(LoginRequiredMixin, generic.UpdateView):
    # template_name = "html file"
    form_class = RequisitionModelForm
    pass


# 4.5 - Delete Requisition
# DeleteView
class DeleteRequisitionView(LoginRequiredMixin, generic.DeleteView):
    pass

# --------------------------------------------------------------- #

# 5 - Transfer
# ListView
# # class TransferListView(generic.ListView):
# #     # template_name = "html file"
# #     queryset = Material_Transfer.objects.all()
# #     context_object_name = "transfer"

# # 5.1 - Add Transfer
# # CreateView
# class AddTransferView(generic.CreateView):
#     # template_name = 'html file'
#     form_class = TransferModelForm
#     pass

# # 5.2 - Update Transfer
# # UpdateView 
# class UpdateTransferView(generic.UpdateView):
#     # template_name = 'html file'
#     form_class = TransferModelForm
#     pass

# 5.3 Delete Transfer 
# DeleteView
#class DeleteTransferView(generic.DeleteView):
#    pass

# --------------------------------------------------------------- #

# 6.1 - Create Site
# CreateView
class CreateSiteView(LoginRequiredMixin, generic.CreateView):
    # template_name = 'html file'
    form_class = SiteModelForm

    def get_success_url(self):
        #return reverse("url")
        pass

    def form_valid(self, form):
        #return super(CreateSiteView, self).form_valid(form)
        pass

def site_create(request):
    #form = SiteModelForm()
    #if request.method == 'POST':
    #    form = SiteModelForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect("url")
    #context = {
    #    "form": form
    #}
    #return render(request, "url", context)
    pass

# 6.2 - List Site
# ListView
class ListSiteView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    context_object_name = "site"

    def get_queryset(self):
        queryset = Site_Item_Inventory.objects.all()
        pass

def site_list(request):
    site = Site.objects.all()
    context = {
        "site": site
    }
    return render (request, "url", context)

# 6.3 - Update Site
# UpdateView
class UpdateSiteView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'html file'
    form_class = SiteModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()

    def get_success_url(self):
        return reverse("url")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Messages")
        return super(UpdateSiteView, self).form_valid(form)

def site_update(request, pk):
    site = Site.objects.get(id=pk)
    form = SiteModelForm


# 6.4 - Delete Site
# DeleteView
class DeleteSiteView(LoginRequiredMixin, generic.DeleteView):
    pass


