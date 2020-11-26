import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone

from main.managers import PlayerManager, CoachManager


class Picture(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='admin pictures', default='default.jpg')

    @property
    def pictureimageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return f'{self.user} Picture'


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Player(models.Model):
    POS = (
        ('goal keeper', 'goal keeper'),
        ('defender', 'defender'),
        ('midfielder', 'midfielder'),
        ('forward', 'forward')
    )
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='player_pics', default='default.jpg')
    position = models.CharField(max_length=200, choices=POS)
    jersey_no = models.ForeignKey('PlayerJersey', on_delete=models.CASCADE, null=True)
    country = CountryField(null=True, blank=True)
    available = models.BooleanField(default=True, editable=True)
    injured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    dob = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    appearances = models.PositiveIntegerField(default=0)
    clean_sheets = models.PositiveIntegerField(default=0)
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
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def injuries(self):
        return self.injury_set.all()

    @property
    def unavailables(self):
        return self.deletedplayer_set.all()


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class PlayerJersey(models.Model):
    NO = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
        (21, 21),
        (22, 22),
        (23, 23),
        (24, 24),
        (25, 25),
        (26, 26),
        (27, 27),
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31),
        (32, 32),
        (33, 33),
        (34, 34),
        (35, 35),
        (36, 36),
        (37, 37),
        (38, 38),
        (39, 39),
        (40, 40),
        (41, 41),
        (42, 42),
        (43, 43),
        (44, 44),
        (45, 45),

    )
    no = models.IntegerField(choices=NO, unique=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Jerseys'

    def __str__(self):
        return str(self.no)


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
    nationality = CountryField(null=True, blank=True)
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

        self.games = self.wins+self.draws+self.losses
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


class Contract(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    daily_pay = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    salary = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    buyout_clause = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    class Meta:
        verbose_name_plural = 'contracts '

    def save(self, *args, **kwargs):
        date_format = "%Y-%m-%d"
        a = datetime.datetime.strptime(str(self.start_date), date_format)
        b = datetime.datetime.strptime(str(self.end_date), date_format)
        self.no_days = (b-a).days
        self.salary = (self.no_days * int(self.daily_pay))
        super().save()

    def get_absolute_url(self):
        return reverse("contract-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.player.user.first_name} {self.player.user.last_name} Contract'


class CoachContract(models.Model):
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.coach.user.first_name} {self.coach.user.last_name}  contract'


class Injury(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    injury_type = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateField(default=timezone.now, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'injuries'

    def get_absolute_url(self):
        return reverse("injury_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.player} ---({self.injury_type})'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.TextField()
    date = models.DateField(default=timezone.now, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("contact-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.email


class Inaccessible(models.Model):
    STATUS = (
        ('sold', 'sold'),
        ('terminated', 'terminated'),
        ('end contract', 'end contract')
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=200)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.player.available = False
        super(Inaccessible, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.player)



