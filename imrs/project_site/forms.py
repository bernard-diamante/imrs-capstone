from django import forms
from .models import Site

class SiteModelForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = (
            'siteName',
            'user',
            'siteStreetNumber',
            'siteStreet',
            'siteBarangay',
            'siteCity',
            'siteProvince',
            'siteRegion',
            'siteZip',
            'siteContactNo'
                )

    def __init__(self, *args, **kwargs):
        super(SiteModelForm, self).__init__(*args, **kwargs)
        self.fields['siteName'].label = "Name"
        self.fields['siteStreetNumber'].label = "Street Number"
        self.fields['siteStreet'].label = "Street"
        self.fields['siteBarangay'].label = "Barangay"
        self.fields['siteCity'].label = "City"
        self.fields['siteProvince'].label = "Province"
        self.fields['siteRegion'].label = "Region"
        self.fields['siteZip'].label = "ZIP Code"
        self.fields['siteContactNo'].label = "Contact Number"
