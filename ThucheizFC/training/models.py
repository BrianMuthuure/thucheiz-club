from django.db import models

# Create your models here.
from django.urls import reverse

from main.models import Player, Coach


class TrainingSession(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('completed', 'completed'),
    )
    date = models.DateField()
    player = models.ManyToManyField(Player, blank=True)
    coach = models.ManyToManyField(Coach, blank=True)
    status = models.CharField(choices=STATUS, max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("training-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.id)
