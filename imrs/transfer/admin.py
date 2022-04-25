from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MaterialTransferItems, MaterialTransfer


admin.site.register(MaterialTransfer)
admin.site.register(MaterialTransferItems)