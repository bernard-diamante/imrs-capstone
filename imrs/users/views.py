from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationsForm
from .models import User


# Create your views here.
class UserCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'accounts/user_create.html'
    form_class = CustomUserCreationsForm
    model = User

    def get_success_url(self):
        return reverse("list-user")

    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "accounts/user_detail.html"
    context_object_name = "users"
    model = User

    def get_queryset(self):
        return User.objects.filter(pk=self.pk)

class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = "accounts/users.html"
    context_object_name = "users"
    model = User

    def get_queryset(self):
        queryset = User.objects.all()

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/user_update.html'
    form_class = UserChangeForm
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.all()

    def get_success_url(self):
        return reverse("list-user")

    def form_valid(self, form):
        form.save()
        return super(UserUpdateView, self).form_valid(form)

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "accounts/user_delete.html"

    def get_success_url(self):
        return reverse("list-user")

    def get_queryset(self):
        user = self.request.user
        return User.objects.all()


