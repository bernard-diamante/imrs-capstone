from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'userFirstName',
            'userMiddleName',
            'userLastName',
            'userSuffix',
            'userEmail',
            'userContactNo',
            'userRole'
            )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationsForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['userFirstName'].label = "First Name"
        self.fields['userMiddleName'].label = "Middle Name"
        self.fields['userLastName'].label = "Last Name"
        self.fields['userSuffix'].label = "Suffix (if needed)"
        self.fields['userEmail'].label = "Email Address"
        self.fields['userContactNo'].label = "Contact No."
        self.fields['userRole'].label = "Role"