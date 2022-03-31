from django import forms
from project_site.models import *


# class TransferModelForm(forms.ModelForm):
#     class Meta:
#         model = Material_Transfer
#         fields = (
#             'originSite',
#         )

class AddSiteItemInventoryModelForm(forms.ModelForm):
    model = Inventory
    fields = (
        'item'
    )

    def __init__(self, *args, **kwargs):
        super(AddSiteItemInventoryModelForm,self).__init__(*args, **kwargs)
        self.fields['item'].label = "Item "

class SiteItemInventoryModelForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            'siteItemCount',
            'siteItemTurnover',
            'siteItemMinThreshold'
        )

    def __init__(self, *args, **kwargs):
        super(SiteItemInventoryModelForm, self).__init__(*args, **kwargs)
        self.fields['siteItemCount'].label = "Count"
        self.fields['siteItemTurnover'].label = "Turnover"
        self.fields['siteItemMinThreshold'].label = "Minimum Threshold"
################################
# renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")