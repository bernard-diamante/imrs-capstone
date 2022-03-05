from django import forms
from .models import *


# class TransferModelForm(forms.ModelForm):
#     class Meta:
#         model = Material_Transfer
#         fields = (
#             'originSiteID',
#         )

class AddSiteItemInventoryModelForm(forms.ModelForm):
    model = Site_Item_Inventory
    fields = (
        'itemID'
    )

    def __init__(self, *args, **kwargs):
        super(AddSiteItemInventoryModelForm,self).__init__(*args, **kwargs)
        self.fields['itemID'].label = "Item ID"

class SiteItemInventoryModelForm(forms.ModelForm):
    class Meta:
        model = Site_Item_Inventory
        fields = (
            'siteItemCount',
            'siteItemTurnover'
        )

    def __init__(self, *args, **kwargs):
        super(SiteItemInventoryModelForm, self).__init__(*args, **kwargs)
        self.fields['siteItemCount'].label = "Item Count"
        self.fields['siteItemTurnover'].label = "Item Turnover"
################################
# renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")