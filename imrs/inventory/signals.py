from django.db.models.signals import pre_save
from .models import Site_Item_Inventory
from django.dispatch import receiver

@receiver(pre_save, sender=Site_Item_Inventory)
def calculate_item_status(sender, instance, **kwargs):
    # If value has not been updated or if item does not exist:
    if instance.siteItemCount == Site_Item_Inventory.objects.filter(pk=instance.pk).values_list('siteItemCount', flat=True):
        pass
    else:
        if instance.siteItemTurnover == 'f':
            instance.siteItemMinThreshold = instance.siteItemMinThreshold * 1.5
        elif instance.siteItemTurnover == 'n':
            instance.siteItemMinThreshold = instance.siteItemMinThreshold * 1.25
        elif instance.siteItemTurnover == 's':
            instance.siteItemMinThreshold = instance.siteItemMinThreshold
            
        if instance.siteItemCount >= instance.siteItemMinThreshold:
            instance.siteItemStatus = 1
        elif (instance.siteItemCount < instance.siteItemMinThreshold) and (instance.siteItemCount > 0):
            instance.siteItemStatus = 2
        else:
            instance.siteItemStatus = 3






# siteItemCount
# siteItemTurnover
# siteItemMinThreshold
# siteItemStatus