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

