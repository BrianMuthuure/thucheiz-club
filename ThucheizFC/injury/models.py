from math import ceil

from django.db import models
from django.utils import timezone

from main.models import Player


class Injury(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    injury_type = models.CharField(max_length=200, blank=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'injuries'

    def __str__(self):
        return f'{self.player}----({self.injury_type})'


class CheckOut(models.Model):
    injury = models.OneToOneField(Injury, on_delete=models.CASCADE)
    check_out_date = models.DateField(null=True, editable=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.check_out_date = timezone.now()
        super(CheckOut, self).save(*args, **kwargs)