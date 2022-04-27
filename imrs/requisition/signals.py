from django.db.models.signals import pre_save, post_save, pre_delete
from project_site.models import Inventory
from django.dispatch import receiver
from transfer.models import MaterialTransfer, MaterialTransferItems
from .models import MaterialRequisition, MaterialRequisitionItems

def update_req_status(instance):
    # If all completed, change req status to delivered.
    req = MaterialRequisition.objects.get(requisition=instance.requisition.pk)
    transfers = MaterialTransfer.objects.filter(requisition__requisition=instance.requisition.pk).values('transferStatus').distinct()
    for transfer in transfers:
        x = transfer.get('transferStatus', 0)
        if x == 0:
            break
        else:
            req.reqStatus = 3
    req.save()

@receiver(pre_save, sender=MaterialTransfer)
def change_requisition_status_pre_save(sender, instance, **kwargs):
    req = MaterialRequisition.objects.get(requisition=instance.requisition.pk)
    if req.reqStatus == 0:
        req.reqStatus = 1
        req.save()
    # If all transfers are delivered, make requisition status delivered
    else:
        update_req_status(instance)
    
@receiver(pre_delete, sender=MaterialTransfer)
def change_requisition_status_pre_delete(sender, instance, **kwargs):
    # On delete of transfer, check if all other transfers are completed.
    update_req_status(instance)

    
# Aggregate count of all transfer item quantities. If req item quantity == aggregated transfer item quantity
@receiver(post_save, sender=MaterialTransfer)
def update_reqitem_count_post_save(sender, created, instance, **kwargs):
    reqItems = MaterialRequisitionItems.objects.filter(requisition=instance.requisition.pk)
    # .values('requisition')
    transferItems = MaterialTransferItems.objects.filter(transfer__requisition=instance.requisition.pk)
    # .values('transfer__requisition')
    # print(reqItems)
    # print(transferItems)
    {'Hotdog log': 100, 'fkajsdf':4092}
    # Requisition hotdog log quantity 100
    # for i in transferItems:
    #     if i.item 
        
    #     print(i.itemQuantity)
    #     print(i.itemQuantity)


    # for i in transferItems:
        # for i in reqItems:
            # if i.item == reqItems.item:
            #   reqItems.itemQuantity -= i.itemQuantity