from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


class User(AbstractUser):
    USER_ROLE_CHOICES = [
        (0, "Admin"),
        (1, "Main Office"),
        (2, "Warehouse Manager"),
        (3, "Site Manager")
    ]
    userID = models.AutoField(primary_key=True) # USE FOR USER LOGIN
    userFirstName = AbstractUser.first_name
    userMiddleName = models.CharField(max_length=50)
    userLastName = AbstractUser.last_name
    userSuffix = models.CharField(max_length=30)
    userType = models.PositiveSmallIntegerField()
    userEmail = AbstractUser.email
    userContactNo = models.CharField(max_length=11)
    userRole = models.PositiveSmallIntegerField(default=3, choices=USER_ROLE_CHOICES)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
    def __str__(self):
        return self.userEmail

class Item(models.Model):
    UNIT_TYPE = [
    # Metric
        ('mm', 'milimeter'),
        ('cm', 'centimeter'),
        ('m', 'meter'),
        ('mg','miligrams'),
        ('g','grams'),
        ('kg','kilograms'),
        
        # Imperial
        ('in', 'inches'),
        ('ft', 'feet'),
        ('lb', 'pound'),
        ('t', 'tonne'),
        ]

    UNIT_CATEGORY = [
        ('d', 'Dimensions'),
        ('w', 'Weight'),
        ('v', 'Volume'),
        ('a', 'Amount'),
        ('e', 'Equipment')
    ]
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    itemCategory = models.CharField(max_length=1, choices=UNIT_CATEGORY, default="Dimensions")
    itemUnitType_1 = models.CharField(max_length=1, choices=UNIT_CATEGORY, default="Dimensions")
    itemUnitType_2 = models.CharField(max_length=2, choices=UNIT_TYPE, null=True, blank=True)
    #itemMaterial = # to clarify

    def __str__(self):
        return self.itemName

class Site(models.Model):
    siteID = models.AutoField(primary_key=True) #change to UUIDField if needed
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) ## added null=True
    siteName = models.CharField(max_length=50, null=True)
    siteLotNo = models.CharField(max_length=30, null=True)
    siteBlockNo = models.CharField(max_length=30, null=True)
    siteBarangay = models.CharField(max_length=30)
    siteCity = models.CharField(max_length=35)
    siteProvince = models.CharField(max_length=30)
    siteRegion = models.CharField(max_length=30)
    siteZip = models.CharField(max_length=10)
    siteContactNo = models.CharField(max_length=11)

# Associative (Inventory - Site)
class Site_Item_Inventory(models.Model):
    ITEM_STATUS = [
        (1,'Normal'),
        (2, 'Low'),
        (3, 'Empty')
    ]
    itemID = models.ForeignKey('Item', on_delete=models.CASCADE)
    siteID = models.OneToOneField('Site', on_delete=models.CASCADE) 
    siteItemCount = models.PositiveIntegerField(default=0)
    siteItemStatus = models.PositiveSmallIntegerField(default=0, choices=ITEM_STATUS)
    
    class Meta:
        UniqueConstraint(fields = ['itemID', 'siteID'], name = 'composite_pk')
    
class Material_Requisition(models.Model):
    REQ_STATUS = [
        (0,'For Review'),
        (1, 'Awaiting Delivery'),
        (2, 'Request Denied'),
        (3, 'Delivered'),
    ]
    reqID = models.AutoField(primary_key=True) #change to UUIDField if needed
    siteID = models.ForeignKey("Site", related_name='destinationSite', on_delete=models.CASCADE) 
    reqDescription = models.CharField(max_length=1000)
    reqDateSubmitted = models.DateTimeField(auto_now=True)
    reqDateNeeded = models.DateTimeField(auto_now=False)
    reqItems = models.ManyToManyField(Item)
    # If error, look up backwards relation
    originSiteID = models.ForeignKey('Site', related_name='originSite', on_delete=models.CASCADE, blank=True, null=True) 

    reqStatus = models.PositiveSmallIntegerField(choices=REQ_STATUS, default=0)
    class Meta:
        UniqueConstraint(fields = ['siteID'], name = 'site_unique')
