from django import forms
from .models import Site

class SiteModelForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = (
            'siteName',
            'userID',
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
            self.fields['siteName'].label = "Site Name"
            self.fields['siteStreetNumber'].label = "Site Street Number"
            self.fields['siteStreet'].label = "Site Street"
            self.fields['siteBarangay'].label = "Site Barangay"
            self.fields['siteCity'].label = "Site City"
            self.fields['siteProvince'].label = "Site Province"
            self.fields['siteRegion'].label = "Site Region"
            self.fields['siteZip'].label = "Site Zip"
            self.fields['siteContactNo'].label = "Site Contact Number"
