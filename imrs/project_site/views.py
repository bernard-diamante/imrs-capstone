from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Site
from .forms import SiteModelForm
from django.views.generic.base import View
 
class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'project_site/site_add.html'
    form_class = SiteModelForm
    model = Site

    def get_success_url(self):
        return reverse_lazy("project_site:list-site")


class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "project_site/site_detail.html"
    context_object_name = "site"
    model = Site

    def get_success_url(self):
        return reverse_lazy("project_site:detail-site")

class SiteDispatchView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        # If the user is warehouse manager/site engineer
        if request.user.role >= 2:
            return render(request, 'project_site/site_detail.html', context={'site': request.user.site, })
        else:
            return SiteListView.as_view()(request)

# If Site Manager, redirect to own Project Site DetailView
class SiteListView(LoginRequiredMixin, generic.ListView):
    template_name = "project_site/site.html"
    context_object_name = "project_sites"
    model = Site


class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'project_site/site_update.html'
    form_class = SiteModelForm
    model = Site

    def get_success_url(self):
        return reverse_lazy("project_site:list-site")

    def form_valid(self, form):
        form.save()
        return super(SiteUpdateView, self).form_valid(form)

class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "project_site/site_delete.html"
    model = Site
    def get_success_url(self):
        return reverse_lazy("project_site:list-site")

