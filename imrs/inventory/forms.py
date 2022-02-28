from django import forms
from .models import *


class RequisitionModelForm(forms.ModelForm):
    class Meta:
        model = Material_Requisition
        fields = (
            'reqDescription',
            'reqDateNeeded'
        )
    # reqform_Description = forms.CharField(label="Reason for Material Requisition", max_length=1000)
    # reqform_DateSubmitted = forms.


class SiteModelForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = (
            'siteName',
            'siteLotNo',
            'siteBlockNo',
            'siteBarangay',
            'siteCity',
            'siteProvince',
            'siteRegion',
            'siteZip',
            'siteContactNo'
        )

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'itemName',
            'itemUnitCategory',
            'itemUnitType',
        )


# class TransferModelForm(forms.ModelForm):
#     class Meta:
#         model = Material_Transfer
#         fields = (
#             'originSiteID',
#         )


class SiteItemInventoryModelForm(forms.ModelForm):
    class Meta:
        model = Site_Item_Inventory
        fields = (
            'siteItemCount',
            'siteItemStatus'
        )
################################
# renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")