from django.db import models
from django.db.models import Q


class NewsQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(date__icontains=query))
        return self.filter(lookups).distinct()


class NewsManager(models.Manager):
    def get_queryset(self):
        return NewsQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)