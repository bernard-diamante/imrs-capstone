from django.db.models.signals import pre_save, post_save
from project_site.models import Inventory
from django.dispatch import receiver
import datetime

@receiver(pre_save, sender=Inventory)
def calculate_item_status_pre_save(sender, instance, **kwargs):
    mult = 0
    if instance.siteItemCount == Inventory.objects.filter(pk=instance.pk).values_list('siteItemCount', flat=True):
        pass
    else:
        if instance.siteItemTurnover == 'F':
            mult = 1.5
        elif instance.siteItemTurnover == 'N':
            mult = 1.25
        elif instance.siteItemTurnover == 'S':
            mult = 1
        # instance.siteItemMinThreshold *= mult

        if instance.siteItemCount == 0: # Added 4/29
            instance.siteItemStatus = 4
        elif instance.siteItemCount >= (instance.siteItemMinThreshold * mult):
            instance.siteItemStatus = 1
        elif (instance.siteItemCount < (instance.siteItemMinThreshold * mult)) and (instance.siteItemCount > 0):
            instance.siteItemStatus = 2
        else:
            instance.siteItemStatus = 3

        # Where is status 0?

@receiver(post_save, sender=Inventory)
def auto_now_inventory_modified(sender, instance, **kwargs):
    instance.inventoryDateModified = datetime.datetime.now()
    # instance.save()