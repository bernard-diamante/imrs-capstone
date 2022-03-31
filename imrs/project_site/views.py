from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Site
from .forms import SiteModelForm
from django.contrib import messages
from django.views.generic.base import View

# Create your views here.
class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'project_site/site_add.html'
    form_class = SiteModelForm
    model = Site

    def get_success_url(self):
        return reverse_lazy("project_site:list-site")

    def form_valid(self, form):
        return super(SiteCreateView, self).form_valid(form)

class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "project_site/site_detail.html"
    context_object_name = "project_sites"
    model = Site

    def get_success_url(self):
        return reverse_lazy("project_site:detail-site")

class SiteDispatchView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.role >= 2:
            # return SiteDetailView.as_view()(request, self.request.user.site)
            # return reverse_lazy("project_site:detail-site", kwargs={'site_pk': 'self.request.user.site'})
            return render(request, 'project_site/site_detail.html', context={'object': request.user, })
        else:
            return SiteListView.as_view()(request)

# If Site Manager, redirect to own Project Site DetailView
class SiteListView(LoginRequiredMixin, generic.ListView):
    template_name = "project_site/site.html"
    context_object_name = "project_sites"
    model = Site

    def get_queryset(self):
        queryset = Site.objects.all()
        return queryset

class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'project_site/site_update.html'
    form_class = SiteModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()

    def get_success_url(self):
        return reverse_lazy("project_site:list-site")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Site has been updated")
        return super(SiteUpdateView, self).form_valid(form)

class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "project_site/site_delete.html"

    def get_success_url(self):
        return reverse_lazy("project_site:list-site")

    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()
