from django.shortcuts import reverse, render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaterialRequisition, MaterialRequisitionItems
from .models import Item
from project_site.models import Inventory
from inventory.views import InventoryListView
from .forms import RequisitionModelForm
from django.contrib import messages
from django.views import generic
from django.db.models import Prefetch
from .forms import RequisitionInlineFormSet, RequisitionItemsModelForm, ReqItemModelForm
from django.views.generic.base import View

# Create your views here.


class RequisitionListView(LoginRequiredMixin, generic.ListView):
    template_name = "requisition/requisition.html"
    context_object_name = "requisition"
    model = MaterialRequisition

    def get_queryset(self):
        qs = MaterialRequisition.objects.all()
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super(RequisitionListView, self).get_context_data(
    #         self, **kwargs)
    #     user = self.request.user

        # return context


class RequisitionAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "requisition/requisition_add.html"
    form_class = RequisitionModelForm
    model = MaterialRequisition
    
    def get_success_url(self):
        return reverse("requisition:list-requisition")
    
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        
        # form.instance.site = self.request.user.site
        if inlines.is_valid() and form.is_valid():
            # req = form.save(commit = False)
            form.instance.site = self.request.user.site
            # req.site = self.request.user.site
            req = form.save()
            inlines.instance = req
            inlines.save()
        # Save the object to commit the changes
        
        # MaterialRequisition.objects.create(
        #     site = self.request.user.site,
        #     reqItems = req.reqItems.set(),
        #     reqDescription = req.reqDescription,
        #     reqDateNeeded = req.reqDateNeeded
        # )
        # else:
        # return self.render_to_response(self.get_context_data(form=form))
        return super(RequisitionAddView, self).form_valid(form)

    def get_queryset(self):
        user = self.request.user
        return MaterialRequisition.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx=super(RequisitionAddView,self).get_context_data(**kwargs)
        ctx['item_list'] = ReqItemModelForm()
        if self.request.method == 'POST':
            ctx['form']=RequisitionModelForm(self.request.POST)
            ctx['inlines']=RequisitionInlineFormSet(self.request.POST)
        else:
            ctx['form']=RequisitionModelForm()
            ctx['inlines']=RequisitionInlineFormSet()
        return ctx

    def get_initial(self):
        initial = super(RequisitionAddView, self).get_initial()
        initial["site"] = self.request.user.site
        return initial
        
        # context['form_class'] = self.form_class
        # context['form_class'].fields["site"].initial = self.request.user.site
        # return context
    



class RequisitionUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
    template_name = "requisition/requisition_update.html"
    form_class = RequisitionModelForm

    def get_queryset(self):
        user = self.request.user
        return MaterialRequisition.objects.all()

    def get_success_url(self):
        return reverse("requisition:list-requisition")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Requisition details have been updated")
        return super(RequisitionUpdateView, self).form_valid(form)


class RequisitionDetailView(LoginRequiredMixin, generic.DetailView): #for main office
    model = MaterialRequisition
    template_name = "requisition/requisition_detail.html"
    context_object_name = "requisition"
    queryset = MaterialRequisition.objects.prefetch_related(
        Prefetch('materialrequisitionitems_set', MaterialRequisitionItems.objects.select_related('item'))
    )

    def get_success_url(self):
        return reverse("requisition:detail-requisition")

    # def get_queryset(self):
    #     reqItems = Material_Requisition.objects.all()
    #     requests = Material_Requisition.objects.filter(pk=self.pk)
    #     # item_list = Item.objects.filter(pk=self.reqItems.itemID)
    #     qs = { 
    #             "requisition": requests,
    #             # "item_list": item_list,
    #             }
    #     return qs
    
    

# class RequisitionDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name = "html file"
#     model = Material_Requisition

#     def get_success_url(self):
#         return reverse("requisition:requisition-list")

#     def get_queryset(self):
#         user = self.request.user
#         return Material_Requisition.objects.all()
