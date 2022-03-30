from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationsForm, CustomUserChangeForm
from .models import User

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationsForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = [
#         'username',
#         'userFirstName',
#         'userMiddleName',
#         'userLastName',
#         'userSuffix',
#         'userEmail',
#         'userContactNo',
#         'userRole'
#         ]

# admin.site.register(User, CustomUserAdmin)