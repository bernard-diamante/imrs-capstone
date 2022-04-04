from django import forms
from .models import *
from project_site.models import Inventory
# from django_select2.forms import Select2MultipleWidget



class TransferModelForm(forms.ModelForm):
    class Meta:
        model = MaterialTransfer
        fields = (
            'requisition.reqDateNeeded',
            'transferItems',
            # 'originSite'
        )
        exclude = ('site',)
        widgets = {
            'requisition.reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            #TextInput(attrs={'style': 'max-width: 600px;', 'placeholder':'Text', 'rows': '3'})
        }
    def __init__(self, *args, **kwargs):
        super(TransferModelForm, self).__init__(*args, **kwargs)
        # self.fields['originSite'].required = True
        self.fields['transferItems'] = forms.ModelMultipleChoiceField(
            queryset=Inventory.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
        self.fields['requisition.reqDateNeeded'].label = "Date Needed"
        self.fields['reqItems'].label = "Requested Items"

        
        
        
        
    # reqform_Description = forms.CharField(label="Reason for Material Requisition", max_length=1000)
    # reqform_DateSubmitted = forms.