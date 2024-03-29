from django.db import models


class Item(models.Model):
    item = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    itemCategory = models.CharField(max_length=50, null=True)
    itemSubcategory = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.itemName

