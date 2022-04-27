from django.shortcuts import reverse, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.views import LoginView


from item.models import Item
from project_site.models import Inventory
from requisition.models import MaterialRequisition
from transfer.models import MaterialTransfer

class DashboardListView(generic.ListView):
    template_name = "dashboard.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
    
        user = self.request.user

        # Add dashboard contents

        return context

    def get_queryset(self):
        qs = {
            'inventory': Inventory.objects.all(),
            'requisition': MaterialRequisition.objects.all(),
            'transfer': MaterialTransfer.objects.all(),
            'delivery': MaterialTransfer.objects.filter(transferStatus=0),
            # '': Item.objects.all(),
        }
        return qs
            
class LandingPageView(generic.TemplateView, LoginRequiredMixin): #Checking if user is logged in
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")
        else:
            return redirect("login")


