from django.db import models
from django.db.models import Q


class FixtureQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
            Q(club__icontains=query) |
            Q(title__icontains=query) |
            Q(opponent__icontains=query) |
            Q(stadium__icontains=query) |
            Q(time__icontains=query) |
            Q(date__icontains=query))
        return self.filter(lookups).distinct()


class FixtureManager(models.Manager):
    def get_queryset(self):
        return FixtureQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)


