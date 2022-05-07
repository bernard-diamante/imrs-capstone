from django.db.models import UniqueConstraint
from item.models import Item
from django.db import models


class MaterialRequisitionItems(models.Model):
    STATUS_CHOICES =[
        ('U', 'Unfilled'),
        ('F', 'Filled')
    ]
    requisition = models.ForeignKey("MaterialRequisition", on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="U")
    itemQuantity = models.PositiveIntegerField(default=0, null=True)
    class Meta:
        UniqueConstraint(fields = ['requisition', 'item'], name = 'req_item_unique')
    def __str__(self):
        return self.item.itemName

class MaterialRequisition(models.Model):
    REQ_STATUS = [
        # Unfilled
        (0,'For Review'),
        # Filled
        (1, 'Partially Filled'),
        (2, 'Request Denied'),
        (3, 'Filled'),
        (4, 'Delivered'),
    ]
    requisition = models.AutoField(primary_key=True) #change to UUField if needed
    site = models.ForeignKey("project_site.Site", on_delete=models.CASCADE) 
    reqDescription = models.TextField(max_length=1000, blank=True)
    reqDateSubmitted = models.DateTimeField(auto_now=True)
    reqDateNeeded = models.DateField(auto_now=False)
    reqItems = models.ManyToManyField(
        Item,
        through="MaterialRequisitionItems",
        through_fields=('requisition', 'item'),
        related_name="mat_req_items"
        )
    reqStatus = models.PositiveSmallIntegerField(choices=REQ_STATUS, default=0)
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    class Meta:
        UniqueConstraint(fields = ['requisition', 'site'], name = 'req_site_unique')
    def __str__(self):
        return str(self.pk)
