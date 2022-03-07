from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from item.models import Item
from project_site.models import Site
# from django.contrib.auth.mixins import LoginRequiredMixin


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
    userEmail = AbstractUser.email
    userContactNo = models.CharField(max_length=11)
    userRole = models.PositiveSmallIntegerField(default=3, choices=USER_ROLE_CHOICES)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
    def __str__(self):
        return self.userEmail

# 


# class CartItem(models.Model):
#     cartItemID = models.OneToOneField('item.Item', on_delete=models.CASCADE, primary_key=True)
#     # is_Ordered = models.BooleanField(default=False)







    
# class Site_Item_Inventory(models.Model):
#     ITEM_STATUS = [
#         (1,'Normal'),
#         (2, 'Low'),
#         (3, 'Empty')
#     ]

#     ITEM_TURNOVER = [
#         ('s', 'Slow'),
#         ('n', 'Normal'),
#         ('f', 'Fast'),
#     ]
    
#     itemID = models.ForeignKey('item.Item', on_delete=models.CASCADE)
#     siteID = models.ForeignKey('project_site.Site', on_delete=models.CASCADE) 
#     siteItemCount = models.PositiveIntegerField(default=0)
#     siteItemStatus = models.PositiveSmallIntegerField(default=1, choices=ITEM_STATUS)
#     siteItemTurnover = models.CharField(max_length=1, choices=ITEM_TURNOVER, default="f")
#     siteItemMinThreshold = models.PositiveSmallIntegerField(default=0)
    
#     class Meta:
#         unique_together = (('itemID', 'siteID'))

