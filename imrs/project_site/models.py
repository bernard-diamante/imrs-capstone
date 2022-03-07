from django.db import models
from imrs import settings


class Site(models.Model):
    siteID = models.AutoField(primary_key=True) 
    userID = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # Form attributes
    siteName = models.CharField(max_length=50, null=True)
    siteStreetNumber = models.CharField(max_length=30, null=True)
    siteStreet = models.CharField(max_length=30, null=True)
    siteBarangay = models.CharField(max_length=30)
    siteCity = models.CharField(max_length=35)
    siteProvince = models.CharField(max_length=30)
    siteRegion = models.CharField(max_length=30)
    siteZip = models.CharField(max_length=10)
    siteContactNo = models.CharField(max_length=11)
