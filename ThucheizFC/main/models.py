import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse

from main.managers import PlayerManager, CoachManager


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Player(models.Model):
    POS = (
        ('gk', 'gk'),
        ('defender', 'defender'),
        ('mid', 'mid'),
        ('forward', 'forward')
    )
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='player_pics', default='default.jpg')
    position = models.CharField(max_length=200, choices=POS)
    nationality = models.CharField(max_length=200, null=True)
    jersey_no = models.PositiveSmallIntegerField(primary_key=True)
    available = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    dob = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    appearances = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(null=True, blank=True, default=0)
    red_cards = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    has_contract = models.BooleanField(default=False)

    objects = PlayerManager()

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        try:
            birthday = self.dob.replace(year=today.year)
        except ValueError:
            birthday = self.dob.replace(year=today.year, month=self.dob.monthl+1, day=1)
        if birthday>today:
            self.age = today.year - self.dob.year - 1
        else:
            self.age = today.year - self.dob.year
        super(Player, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.jersey_no)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Coach(models.Model):
    TITLE = (
        ('Manager', 'Manager'),
        ('Ass Manager', 'Ass Manager'),
        ('Gk Coach', 'GK Coach'),
    )
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='coach_pics', default='default.jpg')
    nationality = models.CharField(max_length=200, null=True)
    title = models.CharField(choices=TITLE, max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    dob = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    trophies = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    games = models.PositiveIntegerField(null=True, blank=True, default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    objects = CoachManager()

    class Meta:
        verbose_name_plural = 'coaches'

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        try:
            birthday = self.dob.replace(year=today.year)
        except ValueError:
            birthday = self.dob.replace(year=today.year, month=self.dob.monthl+1, day=1)
        if birthday > today:
            self.age = today.year - self.dob.year - 1
        else:
            self.age = today.year - self.dob.year
        super(Coach, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("coach-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.user.username

    @property
    def coachimageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class PlayerContract(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    buyout_clause = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    bonuses = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total_salary = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'player contracts '

    def save(self, *args, **kwargs):
        if self.player:
            self.total_salary = self.salary + self.bonuses
        super(PlayerContract, self).save()

    def get_absolute_url(self):
        return reverse("contract-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.player.user.username} Contract'
