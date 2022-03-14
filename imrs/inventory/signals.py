from django.db.models.signals import pre_save
from project_site.models import Inventory
from django.dispatch import receiver

@receiver(pre_save, sender=Inventory)
def calculate_item_status(sender, instance, **kwargs):
    # If value has not been updated or if item does not exist:
    if instance.siteItemCount == Inventory.objects.filter(pk=instance.pk).values_list('siteItemCount', flat=True):
        pass
    else:
        if instance.siteItemTurnover == 'f':
            mult = 1.5
        elif instance.siteItemTurnover == 'n':
            mult = 1.25
        elif instance.siteItemTurnover == 's':
            mult = 1
        instance.siteItemMinThreshold *= mult
            
        if instance.siteItemCount >= instance.siteItemMinThreshold:
            instance.siteItemStatus = 1
        elif (instance.siteItemCount < instance.siteItemMinThreshold) and (instance.siteItemCount > 0):
            instance.siteItemStatus = 2
        else:
            instance.siteItemStatus = 3

