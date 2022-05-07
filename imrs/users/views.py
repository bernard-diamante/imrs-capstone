from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.views.generic.base import View

class UserCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'user/user_add.html'
    form_class = CustomUserCreationForm
    model = User

    def get_success_url(self):
        return reverse_lazy("users:list-user")

    def form_valid(self, form):
        form.clean()
        form.save()
        return super(UserCreateView, self).form_valid(form)
    

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "user/user_detail.html"
    model = User
    context_object_name = 'users'

    def get_success_url(self):
        return reverse_lazy("users:detail-user")

class UserDispatchView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.role >= 2:
            return render(request, 'user/user_detail.html', context={'object': request.user, })
        else:
            return UserListView.as_view()(request)

class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = "user/user.html"
    model = User
    context_object_name = 'users'

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/user_update.html'
    form_class = CustomUserChangeForm
    model = User 

    def get_success_url(self):
        return reverse_lazy("users:list-user")

    def form_valid(self, form):
        form.save()
        return super(UserUpdateView, self).form_valid(form)

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    def get_success_url(self):
        return reverse_lazy("users:list-user")


