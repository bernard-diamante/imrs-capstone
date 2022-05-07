from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from project_site.models import Inventory
from django.dispatch import receiver
from transfer.models import MaterialTransfer, MaterialTransferItems
from .models import MaterialRequisition, MaterialRequisitionItems

def update_req_status(instance):
    # If all completed, change req status to delivered.
    req = MaterialRequisition.objects.get(requisition=instance.requisition.pk)
    req_items = MaterialRequisitionItems.objects.filter(requisition__requisition=instance.requisition.pk)
    # req_items = req.values.all()

    transfers = MaterialTransfer.objects.filter(requisition__requisition=instance.requisition.pk).count()
    transfer_statuses = MaterialTransfer.objects.filter(requisition__requisition=instance.requisition.pk).values('transferStatus').distinct()
    transfer_list = [transfer.get('transferStatus') for transfer in transfer_statuses] # Use list comprehension if possible 
    if transfers == req_items.count(): # If all items are filled
        if 1 in transfer_list and len(transfer_list) == 1: # Set reqStatus to Delivered (reqStatus=4) if all items are delivered
            req.reqStatus = 4
        elif (0 in transfer_list or 1 in transfer_list) and len(transfer_list) >= 1: # Set reqStatus to Filled (reqStatus=3) if not all items are delivered
            req.reqStatus = 3
    # If no transfers, set reqStatus to 0 (For Review)
    elif transfers == 0:
        req.reqStatus = 0
    elif transfers != (req_items.count()): # If not all items are filled
        if 0 in transfer_list or 1 in transfer_list: # Set reqStatus to Partially Filled (reqStatus=1) if none of the items are delivered to the inventory
            req.reqStatus = 1
    req.save()
    

@receiver(post_save, sender=MaterialTransfer)
def change_requisition_status_pre_save(sender, instance, **kwargs):
    # req = MaterialRequisition.objects.get(requisition=instance.requisition.pk)
    # If all transfers are delivered, make requisition status delivered
    update_req_status(instance)
    
@receiver(post_delete, sender=MaterialTransfer)
def change_requisition_status_pre_delete(sender, instance, **kwargs):
    # On delete of transfer, check if all other transfers are completed.
    update_req_status(instance)
