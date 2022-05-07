from django.db.models.signals import pre_save, post_save
from .models import MaterialTransfer
from django.dispatch import receiver
import datetime

@receiver(post_save, sender=MaterialTransfer)
def auto_now_transfer_modified(sender, instance, **kwargs):
    instance.transferDateModified = datetime.datetime.now()


# @receiver(post_save, sender=MaterialTransfer)
# def 