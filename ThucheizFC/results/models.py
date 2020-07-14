from django.db import models

# Create your models here.
from results.managers import ResultManager


class Result(models.Model):
    result_type = models.CharField(max_length=200)
    club = models.CharField(max_length=50, default='Stars')
    club_score = models.PositiveIntegerField(default=0)
    opponent = models.CharField(max_length=100, null=False, blank=False)
    opponent_score = models.PositiveIntegerField(default=0)
    opponent_image = models.ImageField(upload_to='opponent_logos', null=True, blank=True)
    active = models.BooleanField(default=True)
    date = models.DateField()

    objects = ResultManager()

    def __str__(self):
        return self.result_type