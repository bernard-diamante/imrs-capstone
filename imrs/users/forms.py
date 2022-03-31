from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User
from .views import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'email',
            'contact_number',
            'role'
            )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "ID Number"
        self.fields['username'].help_text = "ID No. is strictly 3 digits (e.g. 1 = 001)."
        self.fields['first_name'].label = "First Name"
        self.fields['middle_name'].label = "Middle Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['suffix'].label = "Suffix"
        self.fields['email'].label = "Email Address"
        self.fields['contact_number'].label = "Contact No."
        self.fields['role'].label = "Role"
        self.fields['password1'].help_text = "Your password must contain at least 8 characters."
        self.fields['password2'].help_text = None

    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name, middle_name, last_name = self.cleaned_data['first_name', 'middle_name', 'last_name'].title()
    def clean_first_name(self):
        cleaned_data = super().clean()
        first_name = cleaned_data['first_name'].title()
        return first_name
    def clean_middle_name(self):
        cleaned_data = super().clean()
        middle_name = cleaned_data['middle_name'].title()
        return middle_name
    def clean_last_name(self):
        cleaned_data = super().clean()
        last_name = cleaned_data['last_name'].title()
        return last_name


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'email',
            'contact_number',
            'role'
            )
        exclude = ('password',)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['middle_name'].label = "Middle Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['suffix'].label = "Suffix (if needed)"
        self.fields['email'].label = "Email Address"
        self.fields['contact_number'].label = "Contact No."
        self.fields['role'].label = "Role"
    def clean_first_name(self):
        cleaned_data = super().clean()
        first_name = cleaned_data['first_name'].title()
        return first_name
    def clean_middle_name(self):
        cleaned_data = super().clean()
        middle_name = cleaned_data['middle_name'].title()
        return middle_name
    def clean_last_name(self):
        cleaned_data = super().clean()
        last_name = cleaned_data['last_name'].title()
        return last_name