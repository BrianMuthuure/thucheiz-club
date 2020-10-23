from django.db import models
from django.db.models import Q


class ResultQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
            Q(result_type__icontains=query) |
            Q(opponent__icontains=query) |
            Q(date__icontains=query) |
            Q(stadium__icontains=query))
        return self.filter(lookups).distinct()


class ResultManager(models.Manager):
    def get_queryset(self):
        return ResultQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)


