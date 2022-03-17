from django.db.models import UniqueConstraint
from item.models import Item
from django.db import models


class Material_Requisition_Items(models.Model):
    STATUS_CHOICES =[
        ('U', 'Unfilled'),
        ('F', 'Filled')
    ]
    reqID = models.ForeignKey("Material_Requisition", on_delete=models.CASCADE)
    itemID = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="U")
    itemQuantity = models.PositiveIntegerField(default=0, null=True)
    class Meta:
        UniqueConstraint(fields = ['reqID', 'itemID'], name = 'req_item_unique')

class Material_Requisition(models.Model):
    REQ_STATUS = [
        (0,'For Review'),
        (1, 'Awaiting Delivery'),
        (2, 'Request Denied'),
        (3, 'Delivered'),
    ]
    reqID = models.AutoField(primary_key=True) #change to UUIDField if needed
    siteID = models.ForeignKey("project_site.Site", related_name='destinationSite', on_delete=models.CASCADE)
    reqDescription = models.CharField(max_length=1000, blank=True)
    reqDateSubmitted = models.DateTimeField(auto_now=True)
    reqDateNeeded = models.DateField(auto_now=False)
    reqItems = models.ManyToManyField(
        Item,
        through="Material_Requisition_Items",
        through_fields=('reqID', 'itemID'),
        related_name="mat_req_items"
        )
    # reqItemsID = models.ForeignKey(Material_Requisition_Items, on_delete=models.CASCADE, related_name="req_items", blank=True, null=True)
    # If error, look up backwards relation
    originSiteID = models.ForeignKey('project_site.Site', related_name='originSite', on_delete=models.CASCADE, blank=True, null=True) 

    reqStatus = models.PositiveSmallIntegerField(choices=REQ_STATUS, default=0)
    class Meta:
        UniqueConstraint(fields = ['reqID', 'siteID'], name = 'req_site_unique')


    