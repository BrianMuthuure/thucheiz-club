from django.db import models


# Create your models here.
from django.urls import reverse


class Fixture(models.Model):
    club = models.CharField(default='Stars United', editable=False, max_length=200)
    title = models.CharField(max_length=200, blank=True)
    opponent = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)
    date = models.DateField()
    active = models.BooleanField(default=True)
    time = models.TimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('fixture-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
