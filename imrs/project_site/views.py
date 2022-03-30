from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Site
from .forms import SiteModelForm
from django.contrib import messages

# Create your views here.
class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'project_site/site_add.html'
    form_class = SiteModelForm
    model = Site

    def get_success_url(self):
        return reverse("project_site:list-site")

    def form_valid(self, form):
        return super(SiteCreateView, self).form_valid(form)

class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "project_site/site_detail.html"
    context_object_name = "project_sites"
    model = Site

    def get_success_url(self):
        return reverse("project_site:detail-site")

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
        return reverse("project_site:list-site")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Site has been updated")
        return super(SiteUpdateView, self).form_valid(form)

class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "project_site/site_delete.html"

    def get_success_url(self):
        return reverse("project_site:list-site")

    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()
