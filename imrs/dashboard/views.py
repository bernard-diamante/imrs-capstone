from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from project_site.models import Inventory
from requisition.models import MaterialRequisition
from transfer.models import MaterialTransfer

class DashboardListView(generic.ListView):
    template_name = "dashboard.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        user = self.request.user
        return context

    def get_queryset(self):
        user = self.request.user
        if user.role >= 2: #Queryset for Site Engr. and Warehouse Manager
            qs = {
                'inventory': Inventory.objects.filter(site=user.site, siteItemStatus=2),
                'requisition': MaterialRequisition.objects.filter(site=user.site),
                'transfer': MaterialTransfer.objects.filter(site=user.site, transferStatus=0),
                # 'delivery': MaterialTransfer.objects.filter(transferStatus=0, site=user.site),
            }


        else:
            qs = {
                'inventory': Inventory.objects.all(),
                'requisition': MaterialRequisition.objects.filter(reqStatus=0),
                'transfer': MaterialTransfer.objects.filter(transferStatus=0),
                # 'delivery': MaterialTransfer.objects.filter(transferStatus=0),
            }
        return qs
            
class LandingPageView(generic.TemplateView, LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")
        else:
            return redirect("login")


