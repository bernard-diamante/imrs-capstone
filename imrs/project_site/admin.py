from django.contrib import admin
from .models import Site, Cart, Inventory


admin.site.register(Site)
admin.site.register(Cart)
admin.site.register(Inventory)