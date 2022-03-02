from django import forms
from .models import Item

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'itemName',
            'itemCategory',
            'itemSubcategory',
        )

    def __init__(self, *args, **kwargs):
        super(ItemModelForm, self).__init__(*args, **kwargs)
        self.fields['itemName'].label = "Item Name"
        self.fields['itemCategory'].label = "Item Category"
        self.fields['itemSubcategory'].label = "Item Subcategory"