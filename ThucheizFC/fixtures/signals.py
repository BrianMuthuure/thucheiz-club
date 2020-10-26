import os

from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Fixture


def _delete_file(path):
    """ deleting files from the file system """
    if os.path.isfile(path):
        os.remove(path)


""" delete player images """
@receiver(post_delete, sender=Fixture)
def delete_image_on_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)