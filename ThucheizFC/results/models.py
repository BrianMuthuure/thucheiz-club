from django.db import models
import math
# Create your models here.
from django.db.models.signals import m2m_changed
from django.urls import reverse

from main.models import Player
from results.managers import ResultManager


class Result(models.Model):
    result_type = models.CharField(max_length=200)
    image = models.ImageField(upload_to='opponent_logos', null=True, blank=True)
    club = models.CharField(max_length=50, default='Thucheiz United')
    opponent = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=True)
    club_goal = models.ManyToManyField('ClubGoal', blank=True)
    opponent_goal = models.ManyToManyField('OpponentGoal', blank=True)
    club_score = models.PositiveIntegerField(null=True, blank=True)
    opponent_score = models.PositiveIntegerField(null=True, blank=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()

    objects = ResultManager()

    def get_absolute_url(self):
        return reverse("result-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.result_type

    @property
    def club_score(self):
        club_score = self.club_goal.count()
        return club_score

    @property
    def opponent_score(self):
        opponent_score = self.opponent_goal.count()
        return opponent_score

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ClubGoal(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    minute = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.player} ({self.minute})'


class OpponentGoal(models.Model):
    scorer = models.CharField(max_length=300, null=True, blank=True)
    minute = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.scorer} ({self.minute})'

