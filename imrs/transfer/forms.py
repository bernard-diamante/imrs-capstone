from django import forms
from .models import *
from project_site.models import Inventory
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper
from item.models import Item
from requisition.models import *


class TransferModelForm(forms.ModelForm):
    class Meta:
        model = MaterialTransfer
        fields = (
            'site',
            'transferStatus'
            # 'originSite'
        )
        exclude = (
            'transferItems',
        )
        widgets = {
            # 'requisition.reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            #TextInput(attrs={'style': 'max-width: 600px;', 'placeholder':'Text', 'rows': '3'})
        }
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        super().__init__(*args, **kwargs)
        self.fields['site'].label = "Origin Site"
        self.fields['site'].queryset = self.fields['site'].queryset.order_by('siteName')
        self.fields['transferStatus'].initial = 0
        self.fields['transferStatus'].required = False
        instance = getattr(self, 'instance', None)
        if not (instance and instance.pk):
            self.fields['transferStatus'].widget = forms.HiddenInput()
        
        # print(kwargs)
        



        # self.fields['originSite'].required = True
        # self.fields['items'] = forms.ModelMultipleChoiceField(
        #     queryset=Inventory.objects.all(),
        #     widget=forms.CheckboxSelectMultiple,
        #     )
        # self.fields['requisition__reqDateNeeded'].label = "Date Needed"
                

########################
        
class TransferItemsModelForm(forms.ModelForm):
    transfer = models.AutoField(primary_key=True)
    item = forms.ModelChoiceField(
        queryset=Item.objects.filter())
    itemQuantity = models.PositiveIntegerField(default=0, null=True)
    class Meta:
        model = MaterialTransferItems
        fields = (
            'transfer',
            'item',
            'itemQuantity',
        )
        # widgets = {
        #     'item': Select2Widget
        # }
    def __init__(self, *args, **kwargs):
        req = kwargs.pop('req', None)
        super(TransferItemsModelForm, self).__init__(*args, **kwargs)
        self.fields['item'].label = "Item"
        self.fields['transfer'].label = "Transfer ID"
        self.fields['itemQuantity'].label = "Quantity"
        self.helper = FormHelper()
        self.form_tag = False
        self.fields['item'].queryset = MaterialRequisitionItems.objects.filter(requisition=req)


        # transferItems = MaterialTransferItems.objects.filter(transfer__requisition=instance.requisition.pk)
        # self.fields['item'].queryset = self.fields['item'].queryset.order_by('itemName')





TransferInlineFormSet = forms.inlineformset_factory(
    MaterialTransfer,
    MaterialTransferItems,
    form = TransferItemsModelForm,
    extra=1,
    can_delete=False,
    can_order=False,
    )   


TransferInlineUpdateFormSet = forms.inlineformset_factory(
    MaterialTransfer,
    MaterialTransferItems,
    form = TransferItemsModelForm,
    extra=0,
    can_delete=False,
    can_order=False,
    )   
