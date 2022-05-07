from django.apps import AppConfig
from django.db.models.signals import pre_save

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self):
        from . import signals