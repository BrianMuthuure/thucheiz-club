from django.db import models
import math
# Create your models here.
from django.db.models.signals import m2m_changed
from django.urls import reverse

from main.models import Player
from results.managers import ResultManager


class Result(models.Model):
    result_type = models.CharField(max_length=200)
    club = models.CharField(max_length=50, default='Thucheiz United', editable=False)
    opponent_logo = models.ImageField(upload_to='opponent_logos', null=True, blank=True)
    opponent = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()

    objects = ResultManager()

    def get_absolute_url(self):
        return reverse("result-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.id)

    @property
    def totals(self):
        return self.goalsscored_set.all()

    @property
    def concedes(self):
        return self.goalsconceded_set.all()

    @property
    def club_total(self):
        return self.goalsscored_set.count()

    @property
    def opponent_total(self):
        return self.goalsconceded_set.count()

    @property
    def imageURL(self):
        try:
            url = self.opponent_logo.url
        except:
            url = ''
        return url


class GoalsScored(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    minute = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Goals Sored'

    def __str__(self):
        return str(self.player)


class GoalsConceded(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    scorer = models.CharField(max_length=200, blank=True, null=True)
    minute = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Goals Conceded'

    def __str__(self):
        return str(self.scorer)