from django.db import models
from imrs import settings
from item.models import Item

class Site(models.Model):
    site = models.AutoField(primary_key=True) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    siteCart = models.ManyToManyField(
        'item.Item',
        through='Cart',
        through_fields=('site', 'cartItem'),
        blank=True,
        related_name='siteCart')
    inventory_items = models.ManyToManyField(
        'item.Item',
        through='Inventory',
        through_fields=('site', 'item'),
        blank=True,
        related_name='inventory_items'
        )
    siteName = models.CharField(max_length=50)
    siteStreetNumber = models.CharField(max_length=30, blank=True)
    siteStreet = models.CharField(max_length=30, blank=True)
    siteBarangay = models.CharField(max_length=30)
    siteCity = models.CharField(max_length=35)
    siteProvince = models.CharField(max_length=30)
    siteRegion = models.CharField(max_length=30)
    siteZip = models.CharField(max_length=10, blank=True)
    siteContactNo = models.CharField(max_length=11)
    def __str__(self):
        return self.siteName

class Cart(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cartItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    cartItemCount = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('cartItem', 'site'))

class Inventory(models.Model):
    ITEM_STATUS = [
        (0, 'Above Threshold'),
        (1, 'Moderate'),
        (2, 'Low'),
        (3, 'Critical'),
        (4, 'Empty')
    ]

    ITEM_TURNOVER = [
        ('S', 'Slow'),
        ('N', 'Normal'),
        ('F', 'Fast'),
    ]
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    
    siteItemCount = models.PositiveIntegerField(default=0)
    siteItemStatus = models.PositiveSmallIntegerField(default=1, choices=ITEM_STATUS)
    siteItemTurnover = models.CharField(max_length=1, choices=ITEM_TURNOVER, default="F")
    siteItemMinThreshold = models.PositiveSmallIntegerField(default=0)
    inventoryDateModified = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item', 'site'], name='unique_item_inv')
        ]
    def __str__(self):
        return self.item.itemName
    
