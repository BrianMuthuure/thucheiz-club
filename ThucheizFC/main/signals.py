import os
import csv
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Player, Inaccessible


def _delete_file(path):
    """ deleting files from the file system """
    if os.path.isfile(path):
        os.remove(path)


""" delete player images """
@receiver(post_delete, sender=Player)
def delete_image_on_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)


""" delete user after deleting player model"""
@receiver(post_delete, sender=Player)
def delete_users_on_delete(sender, instance, *args, **kwargs):
    instance.user.delete()


""" delete user after deleting player model"""
@receiver(post_delete, sender=Inaccessible)
def delete_players_on_delete(sender, instance, *args, **kwargs):
    instance.player.delete()
