from django import forms
from .models import Item

class UpdateItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'itemCategory',
            'itemSubcategory',
        )

    def __init__(self, *args, **kwargs):
        super(UpdateItemModelForm, self).__init__(*args, **kwargs)
        self.fields['itemCategory'].label = "Category"
        self.fields['itemSubcategory'].label = "Subcategory"

class AddItemModelForm(forms.ModelForm):
    # item = forms.IntegerField(min_value=0)
    class Meta:
        model = Item
        fields = (
            'itemName',
            'itemCategory',
            'itemSubcategory',
        )

    def __init__(self, *args, **kwargs):
        super(AddItemModelForm, self).__init__(*args, **kwargs)
        self.fields['itemName'].label = "Name"
        self.fields['itemCategory'].label = "Category"
        self.fields['itemSubcategory'].label = "Subcategory"