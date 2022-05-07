from django.db import models
from item.models import Item
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError

class MaterialTransferItems(models.Model):
    transfer = models.ForeignKey("MaterialTransfer", on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    itemQuantity = models.PositiveIntegerField(default=0, null=True)
    class Meta:
        UniqueConstraint(fields = ['transfer', 'item'], name = 'req_item_unique')
    def __str__(self):
        return self.item.itemName


class MaterialTransfer(models.Model):
    TRAN_STATUS = [
        (0, 'Awaiting Approval'),
        (1, 'Approved'),
        (2, 'Delivered')
    ]
    transfer = models.AutoField(primary_key=True)
    # destination site accessed through requisition forms
    requisition = models.ForeignKey("requisition.MaterialRequisition", on_delete = models.CASCADE)
    # origin site
    site = models.ForeignKey('project_site.Site', on_delete=models.CASCADE)
    transferItems = models.ManyToManyField(
        Item,
        through="MaterialTransferItems",
        through_fields=('transfer', 'item'),
        related_name="mat_tran_items"
        )
    transferDateSubmitted = models.DateField(auto_now=True)
    transferStatus = models.PositiveSmallIntegerField(choices=TRAN_STATUS, default=0)
    transferDateModified = models.DateTimeField(blank=True, null=True)
