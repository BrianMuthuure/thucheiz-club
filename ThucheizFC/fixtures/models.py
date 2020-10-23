from django.db import models


# Create your models here.
from django.urls import reverse

from fixtures.managers import FixtureManager


class Fixture(models.Model):
    club = models.CharField(default='Thucheiz United', max_length=200)
    title = models.CharField(max_length=200, blank=True)
    opponent = models.CharField(max_length=200)
    opponent_image = models.ImageField(upload_to='logos', default='logo.png')
    stadium = models.CharField(max_length=200)
    date = models.DateField()
    active = models.BooleanField(default=True)
    time = models.TimeField(blank=True, null=True)

    objects = FixtureManager()

    def get_absolute_url(self):
        return reverse('fixture-detail', kwargs={'pk': self.pk})

    @property
    def fixtureimageURL(self):
        try:
            url = self.opponent_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title
