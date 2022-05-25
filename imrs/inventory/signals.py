from django.db.models.signals import pre_save, post_save
from project_site.models import Inventory
# from transfer.models import MaterialTransfer
from django.dispatch import receiver
import datetime

@receiver(pre_save, sender=Inventory)
def calculate_item_status_pre_save(sender, instance, **kwargs):
    mult = 0
    if instance.siteItemCount == Inventory.objects.filter(pk=instance.pk).values_list('siteItemCount', flat=True):
        pass
    else:
        if instance.siteItemTurnover == 'F':
            mult = 1
        elif instance.siteItemTurnover == 'N':
            mult = 0.8
        elif instance.siteItemTurnover == 'S':
            mult = 0.6

        # Change status based on item count and turnover
        if instance.siteItemCount == 0: # Added 4/29
            instance.siteItemStatus = 4
        elif instance.siteItemCount >= (instance.siteItemMinThreshold * mult):
            instance.siteItemStatus = 0

        elif instance.siteItemCount >= (instance.siteItemMinThreshold * mult * 0.75):
            instance.siteItemStatus = 1
        elif instance.siteItemCount >= (instance.siteItemMinThreshold * mult * 0.50):
            instance.siteItemStatus = 2
        elif instance.siteItemCount >= (instance.siteItemMinThreshold * mult * 0.25):
            instance.siteItemStatus = 3
    

@receiver(post_save, sender=Inventory)
def auto_now_inventory_modified(sender, instance, **kwargs):
    instance.inventoryDateModified = datetime.datetime.now()
    # instance.save()