from django.db import models
from item.models import Item
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError

# Create your models here.
class MaterialTransferItems(models.Model):
    transfer = models.ForeignKey("MaterialTransfer", on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    itemQuantity = models.PositiveIntegerField(default=0, null=True)
    class Meta:
        UniqueConstraint(fields = ['transfer', 'item'], name = 'req_item_unique')


class MaterialTransfer(models.Model):
    TRAN_STATUS = [
        (0,'For Review'),
        (1, 'Awaiting Delivery'),
        (2, 'Transfer Pending'),
        (3, 'Transfer Accomplished'),
    ]
    transfer = models.AutoField(primary_key=True)
    requisition = models.ForeignKey("requisition.MaterialRequisition", on_delete = models.CASCADE)
    site = models.ForeignKey('project_site.Site', on_delete=models.CASCADE)
    transferItems = models.ManyToManyField(
        Item,
        through="MaterialTransferItems",
        through_fields=('transfer', 'item'),
        related_name="mat_tran_items"
        )
    transferDateSubmitted = models.DateField(auto_now=False)
    transferStatus = models.PositiveSmallIntegerField(choices=TRAN_STATUS, default=0)
    def clean(self):
        if self.site_id == self.site:
            raise ValidationError("Site cannot send item to themselves.")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    # class Meta:
    #     UniqueConstraint(fields = ['transfer', 'requisition'], name = 'tran_req_unique')
