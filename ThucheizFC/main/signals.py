import os
import csv
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Player, Contract

""" create contract after the player is saved """
@receiver(post_save, sender=Player)
def create_contract(sender, instance, created, **kwargs):
    if created:
        Contract.objects.create(player=instance)
        print(sender)


@receiver(post_save, sender=Player)
def save_contract(sender, instance, **kwargs):
    instance.contract.save()
    print(sender)


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
