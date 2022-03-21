from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# Create your views here.
# class DashboardListView(generic.ListView):
#     template_name = "dashboard.html"

#     def get_context_data(self, **kwargs):
#         context = super(DashboardListView, self).get_context_data(**kwargs)

#         user = self.request.user

#         # Add dashboard contents

#         return context

