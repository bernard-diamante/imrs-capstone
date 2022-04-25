from django import forms
from .models import *
from project_site.models import Inventory
from django_select2 import forms as s2forms
from django_select2.forms import Select2Widget
from django.forms import formset_factory
from item.models import Item
from project_site.models import Site
from django.db import transaction
from crispy_forms.helper import FormHelper
# import select2
# from crispy_forms.helper import FormHelper
# from django_select2.forms import Select2MultipleWidget



class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisition
        fields = (
            'reqDescription',
            'reqDateNeeded',
            # 'reqStatus'
        )
        widgets = {
            'reqDateNeeded': forms.DateInput(attrs={'type': 'date'}),
            'reqDescription':forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.requisition_formset = RequisitionInlineFormSet(
            data=kwargs.get('data'), instance=self.instance
        )
        self.helper = FormHelper()
        self.form_tag = False
        
        self.fields['reqDescription'].label = "Description"
        self.fields['reqDateNeeded'].label = "Date Needed"
        

    # def save(self, **kwargs):
    #     with transaction.atomic():
    #         saved_req = super().save(**kwargs)
    #         self.requisition_formset.instance = saved_req
    #         self.requisition_formset.save()
    #         return saved_req

    # def clean(self):
    #     self.requisition_formset.clean()
    #     super().clean()
    #     return self.cleaned_data

    # def is_valid(self):
    #     is_valid = True
    #     is_valid &= self.requisition_formset.is_valid()
    #     is_valid &= super().is_valid()
    #     return is_valid

    # def has_changed(self):
    #     has_changed = False
    #     has_changed |= self.requisition_formset.has_changed()
    #     has_changed |= super().has_changed
    #     return has_changed
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

    # item = select2.fields.ChoiceField(
    #     choices=Item.objects.as_choices(),
    #     overlay="Select an Item")

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


# class ValidRequisitionFormSet(RequisitionInlineFormSet):
#     def clean(self):
#         if 
#             for form in self.forms:
#                 form.clean()



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