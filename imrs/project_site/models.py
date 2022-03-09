from django.db import models
# from inventory.models import CartItem
from imrs import settings


class Site(models.Model):
    siteID = models.AutoField(primary_key=True) 
    userID = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    siteCart = models.ManyToManyField(
        'item.Item',
        through='Cart',
        through_fields=('siteID', 'cartItemID'),
        blank=True,
        related_name='siteCart')
    inventory_items = models.ManyToManyField(
        'item.Item',
        through='Inventory',
        through_fields=('siteID', 'itemID'),
        blank=True,
        related_name='inventory_items')
    siteName = models.CharField(max_length=50)
    siteStreetNumber = models.CharField(max_length=30, blank=True)
    siteStreet = models.CharField(max_length=30, blank=True)
    siteBarangay = models.CharField(max_length=30)
    siteCity = models.CharField(max_length=35)
    siteProvince = models.CharField(max_length=30)
    siteRegion = models.CharField(max_length=30)
    siteZip = models.CharField(max_length=10, blank=True)
    siteContactNo = models.CharField(max_length=11)

class Cart(models.Model):
    siteID = models.ForeignKey(Site, on_delete=models.CASCADE)
    cartItemID = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    class Meta:
        unique_together = (('cartItemID', 'siteID'))

class Inventory(models.Model):
    ITEM_STATUS = [
        (1,'Normal'),
        (2, 'Low'),
        (3, 'Empty')
    ]

    ITEM_TURNOVER = [
        ('S', 'Slow'),
        ('N', 'Normal'),
        ('F', 'Fast'),
    ]
    itemID = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    siteID = models.ForeignKey(Site, on_delete=models.CASCADE)
    
    siteItemCount = models.PositiveIntegerField(default=0)
    siteItemStatus = models.PositiveSmallIntegerField(default=1, choices=ITEM_STATUS)
    siteItemTurnover = models.CharField(max_length=1, choices=ITEM_TURNOVER, default="F")
    siteItemMinThreshold = models.PositiveSmallIntegerField(default=0)

    class Meta:
        # unique_together = (('itemID', 'siteID'))
        constraints = [
            models.UniqueConstraint(fields=['itemID', 'siteID'], name='unique_item_inv')
        ]
