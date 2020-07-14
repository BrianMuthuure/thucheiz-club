from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from news.managers import NewsManager


class News(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='news_pics')
    active = models.BooleanField(default=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    objects = NewsManager()

    class Meta:
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url