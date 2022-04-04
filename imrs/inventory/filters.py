import django_filters
from project_site.models import Inventory, Site



# class InventoryFilter(django_filters.FilterSet):
#     class Meta:
#         model = Inventory
#         fields = ('')

class InventoryFilter(django_filters.FilterSet):
    site = django_filters.ModelChoiceFilter(queryset=Site.objects.all())

    class Meta:
        model = Inventory
        fields = [
            'site'
            # 'siteItemCount',
            # 'item.itemCategory',
            # 'item.itemSubcategory',
            # 'siteItemTurnover',
            # 'siteItemStatus'
        ]


