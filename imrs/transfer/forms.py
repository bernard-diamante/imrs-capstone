from django import forms
from .models import *
from project_site.models import Inventory
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper



class TransferModelForm(forms.ModelForm):
    class Meta:
        model = MaterialTransfer
        fields = (
            'transferItems',
            'site',
            'transferStatus',
            # 'originSite'
        )
        widgets = {
            # 'requisition.reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            #TextInput(attrs={'style': 'max-width: 600px;', 'placeholder':'Text', 'rows': '3'})
        }
    def __init__(self, *args, **kwargs):
        super(TransferModelForm, self).__init__(*args, **kwargs)
        # self.fields['originSite'].required = True
        self.fields['transferItems'] = forms.ModelMultipleChoiceField(
            queryset=Inventory.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
        # self.fields['requisition__reqDateNeeded'].label = "Date Needed"
        self.fields['transferItems'].label = "Transferred Items"
        self.fields['site'].label = "Origin Site"

########################
        
class TransferItemsModelForm(forms.ModelForm):
    class Meta:
        model = MaterialTransferItems
        fields = (
            'transfer',
            'item',
            'itemQuantity',
        )
        widgets = {
            'item': Select2Widget
        }
    def __init__(self,*args, **kwargs):
        super(TransferItemsModelForm, self).__init__(*args, **kwargs)
        self.fields['item'].label = "Item"
        self.fields['transfer'].label = "Transfer ID"
        self.fields['itemQuantity'].label = "Quantity"
        self.helper = FormHelper()
        self.form_tag = False
            
TransferInlineFormSet = forms.inlineformset_factory(
    MaterialTransfer,
    MaterialTransferItems,
    form = TransferItemsModelForm,
    extra=1,
    can_delete=False,
    can_order=False,
    )   
        