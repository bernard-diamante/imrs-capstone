from django import forms
from .models import *
from django_select2.forms import Select2Widget
from item.models import Item
from crispy_forms.helper import FormHelper

class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisition
        fields = (
            'reqDescription',
            'reqDateNeeded',
        )
        widgets = {
            'reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            'reqDescription':forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_tag = False
        
        self.fields['reqDescription'].label = "Description"
        self.fields['reqDateNeeded'].label = "Date Needed"

class RequisitionItemsModelForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisitionItems
        fields = (
            'requisition',
            'item',
            'itemQuantity',
        )
        widgets = {
            'item': Select2Widget
        }
    def __init__(self,*args, **kwargs):
        super(RequisitionItemsModelForm, self).__init__(*args, **kwargs)
        self.fields['item'].label = "Item"
        self.fields['requisition'].label = "Requisition ID"
        self.fields['itemQuantity'].label = "Quantity"
        self.helper = FormHelper()
        self.form_tag = False
        self.fields['item'].queryset = self.fields['item'].queryset.order_by('itemName')

    @property
    def media(self):
        return forms.Media(css={'all': ('pretty.css',)},
                           js=('animations.js', 'actions.js'))
        

RequisitionInlineFormSet = forms.inlineformset_factory(
    MaterialRequisition,
    MaterialRequisitionItems,
    form = RequisitionItemsModelForm,
    extra=1,
    can_delete=False,
    can_order=False,
    )

class ReqItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item']
        widgets = {
            'item': Select2Widget
        }