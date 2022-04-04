from django import forms
from .models import *
from project_site.models import Inventory
# from django_select2.forms import Select2MultipleWidget



class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisition
        fields = (
            'reqDescription',
            'reqDateNeeded',
            'reqItems',
            # 'originSite'
        )
        exclude = ('site',)
        widgets = {
            'reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            'reqDescription':forms.Textarea(attrs={'rows': 3})
            #TextInput(attrs={'style': 'max-width: 600px;', 'placeholder':'Text', 'rows': '3'})
        }
    def __init__(self, *args, **kwargs):
        super(RequisitionModelForm, self).__init__(*args, **kwargs)
        # self.fields['originSite'].required = True
        self.fields['reqItems'] = forms.ModelMultipleChoiceField(
            queryset=Inventory.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
        self.fields['reqDescription'].label = "Description"
        self.fields['reqDateNeeded'].label = "Date Needed"
        self.fields['reqItems'].label = "Requested Items"

        
       
        
    # reqform_Description = forms.CharField(label="Reason for Material Requisition", max_length=1000)
    # reqform_DateSubmitted = forms.