from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Player, Contract


@receiver(post_save, sender=Player)
def create_contract(sender, instance, created, **kwargs):
    if created:
        Contract.objects.create(player=instance)
        print(sender)


@receiver(post_save, sender=Player)
def save_contract(sender, instance, **kwargs):
    instance.contract.save()
    print(sender)