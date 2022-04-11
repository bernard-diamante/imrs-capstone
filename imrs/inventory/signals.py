from django.db.models.signals import pre_save, post_save
from project_site.models import Inventory
from django.dispatch import receiver

@receiver(pre_save, sender=Inventory)
def calculate_item_status_pre_save(sender, instance, **kwargs):
    mult = 0
    # If value has not been updated or if item does not exist:
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
            
        if instance.siteItemCount >= (instance.siteItemMinThreshold * mult):
            instance.siteItemStatus = 1
        elif (instance.siteItemCount < (instance.siteItemMinThreshold * mult)) and (instance.siteItemCount > 0):
            instance.siteItemStatus = 2
        else:
            instance.siteItemStatus = 3
        print("STATUS UPDATED")

@receiver(post_save, sender=Inventory)
def calculate_item_status_post_save(sender, created, instance, **kwargs):
    if created:
        print("Status is", instance.siteItemStatus)
        instance.save()
    else:
        print(instance.siteItemStatus, "was just saved")