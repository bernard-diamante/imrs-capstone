from django import forms
from .models import *
from project_site.models import Inventory
from django_select2 import forms as s2forms
from django_select2.forms import Select2Widget
from django.forms import formset_factory
from item.models import Item
from project_site.models import Site
# from crispy_forms.helper import FormHelper
# from django_select2.forms import Select2MultipleWidget



class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisition
        fields = (
            'reqDescription',
            'reqDateNeeded',
            'reqStatus'
        )
        widgets = {
            'reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            'reqDescription':forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request')
        super(RequisitionModelForm, self).__init__(*args, **kwargs)
        
        # kwargs.update({
        #     'initial': {
        #         'site': self.request.user.site
        #     }
        # })
        

        # self.fields['reqItems'].widget = forms.CheckboxSelectMultiple(attrs={
        #         'required': True,
        #         'class': 'date-time-picker',
        #         'data-options': '{"format":"Y-m-d H:i", "timepicker":"true"}'
        #     })

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
    # reqform_Description = forms.CharField(label="Reason for Material Requisition", max_length=1000)
    # reqform_DateSubmitted = forms.

RequisitionInlineFormSet = forms.inlineformset_factory(
    MaterialRequisition,
    MaterialRequisitionItems,
    form = RequisitionItemsModelForm,
    extra=1,
    can_delete=False,
    can_order=False,
    )



class ReqItemModelForm(forms.ModelForm):
    # items = forms.ModelChoiceField(queryset = Item.objects.all().order_by('item'))
    class Meta:
        model = Item
        fields = ['item']
        widgets = {
            'item': Select2Widget

        }

# RequisitionItemsFormset = forms.modelformset_factory(
#     ReqItemModelForm,
#     fields=('item','itemQuantity'),
#     widgets = {
#             'item': Select2Widget
#         }
# )