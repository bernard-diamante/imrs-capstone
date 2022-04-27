from django.apps import AppConfig
from django.db.models.signals import pre_save

class RequisitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requisition'

    def ready(self):
        from . import signals