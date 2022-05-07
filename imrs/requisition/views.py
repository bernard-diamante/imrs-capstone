from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaterialRequisition, MaterialRequisitionItems
from django.views import generic
from django.db.models import Prefetch
from .forms import RequisitionInlineFormSet, ReqItemModelForm, RequisitionModelForm
from django.urls import reverse_lazy


class RequisitionListView(LoginRequiredMixin, generic.ListView):
    template_name = "requisition/requisition.html"
    context_object_name = "requisition"
    model = MaterialRequisition

    def get_queryset(self):
        if self.request.user.role >= 2: 
            qs = {
                "requests": MaterialRequisition.objects.filter(site__site=self.request.user.site.site),
            }      
        else:
            qs = {
                "requests": MaterialRequisition.objects.all(),
            }
        return qs

class RequisitionAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "requisition/requisition_add.html"
    form_class = RequisitionModelForm
    model = MaterialRequisition
    
    def get_success_url(self):
        return reverse_lazy("requisition:list-requisition")
    
    def form_valid(self, form):
        print(form.data)
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            form.instance.site = self.request.user.site
            req = form.save()
            inlines.instance = req
            inlines.save()
        return super(RequisitionAddView, self).form_valid(form)
    
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

class RequisitionUpdateView(LoginRequiredMixin, generic.UpdateView): #for main office
    template_name = "requisition/requisition_update.html"
    form_class = RequisitionModelForm
    model = MaterialRequisition

    def get_success_url(self):
        return reverse_lazy("requisition:list-requisition")

    def form_valid(self, form):
        form.save()
        return super(RequisitionUpdateView, self).form_valid(form)


class RequisitionDetailView(LoginRequiredMixin, generic.DetailView): #for main office
    model = MaterialRequisition
    template_name = "requisition/requisition_detail.html"
    context_object_name = "requisition"
    queryset = MaterialRequisition.objects.prefetch_related(
        Prefetch('materialrequisitionitems_set', MaterialRequisitionItems.objects.select_related('item'))
    )

    def get_success_url(self):
        return reverse_lazy("requisition:detail-requisition")
