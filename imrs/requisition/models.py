from django.db.models import UniqueConstraint
from item.models import Item
from django.db import models
from project_site.models import Site

class Material_Requisition(models.Model):
    REQ_STATUS = [
        (0,'For Review'),
        (1, 'Awaiting Delivery'),
        (2, 'Request Denied'),
        (3, 'Delivered'),
    ]
    reqID = models.AutoField(primary_key=True) #change to UUIDField if needed
    siteID = models.ForeignKey("project_site.Site", related_name='destinationSite', on_delete=models.CASCADE) 
    reqDescription = models.CharField(max_length=1000)
    reqDateSubmitted = models.DateTimeField(auto_now=True)
    reqDateNeeded = models.DateTimeField(auto_now=False)
    reqItems = models.ManyToManyField(Item)
    # If error, look up backwards relation
    originSiteID = models.ForeignKey('project_site.Site', related_name='originSite', on_delete=models.CASCADE, blank=True, null=True) 

    reqStatus = models.PositiveSmallIntegerField(choices=REQ_STATUS, default=0)
    class Meta:
        UniqueConstraint(fields = ['siteID'], name = 'site_unique')