from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# Create your views here.
# class SignupView(generic.CreateView):
#     template_name = 'user/user_add.html'
#     form_class = UserCreationForm
#     def get_success_url(self):
#         return reverse('login')
class UserCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'user/user_add.html'
    form_class = CustomUserCreationForm
    model = User

    def get_success_url(self):
        return reverse("users:list-user")

    def form_valid(self, form):
        form.clean()
        form.save()
        return super(UserCreateView, self).form_valid(form)
    

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "user/user_detail.html"
    model = User
    context_object_name = 'users'

    def get_success_url(self):
        return reverse("users:detail-user")
    # def get_queryset(self):
    #     return User.objects.get(pk=self.pk)

class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = "user/user.html"
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        qs = User.objects.all()
        return qs


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/user_update.html'
    form_class = CustomUserChangeForm
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.all()

    def get_success_url(self):
        return reverse("users:list-user")

    def form_valid(self, form):
        form.save()
        return super(UserUpdateView, self).form_valid(form)

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "user/user_delete.html"

    def get_success_url(self):
        return reverse("users:list-user")

    def get_queryset(self):
        user = self.request.user
        return User.objects.all()


