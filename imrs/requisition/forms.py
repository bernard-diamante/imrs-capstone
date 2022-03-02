from django import forms
from .models import *


class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = Material_Requisition
        fields = (
            'reqDescription',
            'reqDateNeeded'
        )
        def __init__(self, *args, **kwargs):
            super(RequisitionModelForm, self).__init__(*args, **kwargs)
            self.fields['reqDescription'].label = "Requisition Description"
            self.fields['reqDateNeeded'].label = "Requisition Date Needed"
    # reqform_Description = forms.CharField(label="Reason for Material Requisition", max_length=1000)
    # reqform_DateSubmitted = forms.
