from django.db import models

# Create your models here.
class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    itemCategory = models.CharField(max_length=50, null=True)
    itemSubcategory = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.itemName

