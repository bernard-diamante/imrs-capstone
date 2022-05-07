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
        )
        # exclude = (
        #     'transferItems',
        # )
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_tag = False
        self.fields['site'].label = "Origin Site"
        self.fields['site'].queryset = self.fields['site'].queryset.order_by('siteName')
        self.fields['transferStatus'].initial = 0
        self.fields['transferStatus'].required = False
        instance = getattr(self, 'instance', None)
        if not (instance and instance.pk):
            self.fields['transferStatus'].widget = forms.HiddenInput()
        
class TransferItemsModelForm(forms.ModelForm):
    # transfer = models.AutoField(primary_key=True)
    # itemQuantity = models.PositiveIntegerField(default=0, null=True)
    # item = forms.ModelChoiceField(queryset=MaterialTransfer.objects.filter())
    class Meta:
        model = MaterialTransferItems
        fields = (
            'transfer',
            'item',
            'itemQuantity',
        )
    def __init__(self, *args, **kwargs):
        reqs = kwargs.pop('reqs', None)
        # items = kwargs.pop('items', None)
        super(TransferItemsModelForm, self).__init__(*args, **kwargs)
        self.fields['item'].label = "Item"
        # self.fields['transfer'].label = "Transfer ID"
        self.fields['itemQuantity'].label = "Quantity"
        self.helper = FormHelper()
        self.form_tag = False
        self.fields['item'].queryset = Item.objects.filter(item__in=reqs)
        # print(self.fields['item'].queryset)
        
        # self.fields['item'].queryset = MaterialRequisitionItems.objects.filter(requisition=req)
        # self.fields['item'].queryset = Item.objects.filter(materialrequisitionitems_set=)
        # self.fields['item'].queryset = self.fields['item'].queryset.filter(item__in=MaterialRequisitionItems.objects.filter(requisition=req))
        # print(Item.objects.filter(item=MaterialRequisitionItems.objects.filter(requisition=req).values('item__item')))
        # x = list(MaterialRequisitionItems.objects.filter(requisition=req).values_list('item__item', flat=True))
        # print(x)
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

   
class EngineerTransferModelForm(forms.ModelForm):
    class Meta:
        model = MaterialTransfer
        fields = (
            'transferStatus',
        )
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        super().__init__(*args, **kwargs)
        self.fields['transferStatus'].label = "Transfer Status"