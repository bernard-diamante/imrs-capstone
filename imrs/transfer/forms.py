from django import forms
from .models import *
from project_site.models import Inventory
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper
from item.models import Item


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
        self.fields['site'].queryset = self.fields['site'].queryset.order_by('siteName')
        

########################
        
class TransferItemsModelForm(forms.ModelForm):
    # transfer = models.AutoField(primary_key=True)
    # item = select2.fields.ChoiceField(
    #     choices=Item.objects.as_choices(),
    #     overlay="Choose an item...")
    # itemQuantity = models.PositiveIntegerField(default=0, null=True)
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
        # self.fields['item'].queryset = self.fields['item'].queryset.order_by('itemName')
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

class TranItemModelForm(forms.ModelForm):
    # items = forms.ModelChoiceField(queryset = Item.objects.all().order_by('item'))
    class Meta:
        model = Item
        fields = ['item']
        widgets = {
            'item': Select2Widget
        }