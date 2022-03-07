from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Site
from .forms import SiteModelForm
from django.contrib import messages

# Create your views here.
class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'html file'
    form_class = SiteModelForm

    def get_success_url(self):
        return reverse("site-list")

    def form_valid(self, form):
        return super(SiteCreateView, self).form_valid(form)

class SiteListView(LoginRequiredMixin, generic.ListView):
    template_name = "html file"
    context_object_name = "site"

    def get_queryset(self):
        queryset = Site.objects.all()

class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'html file'
    form_class = SiteModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()

    def get_success_url(self):
        return reverse("site-list")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Site has been updated")
        return super(SiteUpdateView, self).form_valid(form)

class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "html file"

    def get_success_url(self):
        return reverse("site-list")

    def get_queryset(self):
        user = self.request.user
        return Site.objects.all()
