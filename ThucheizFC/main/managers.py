from django.db import models
from django.db.models import Q


class PlayerQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def available(self):
        return self.filter(available=True, active=True)

    def injured(self):
        return self.filter(available=False, active=True)

    def has_contract(self):
        return self.filter(has_contract=False, active=True)

    def search(self, query):
        lookups = (
            Q(position__icontains=query) |
            Q(nationality__icontains=query) |
            Q(age__icontains=query) |
            Q(jersey_no__iexact=query)
        )
        return self.filter(lookups).distinct()


class PlayerManager(models.Manager):
    def get_queryset(self):
        return PlayerQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()

    def available(self):
        return self.get_queryset().available()

    def has_contract(self):
        return self.get_queryset().has_contract()

    def injured(self):
        return self.get_queryset().injured()

    def search(self, query):
        return self.get_queryset().search(query)


class CoachQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
                Q(nationality__icontains=query) |
                Q(age__icontains=query) |
                Q(title__icontains=query))
        return self.filter(lookups).distinct()


class CoachManager(models.Manager):
    def get_queryset(self):
        return CoachQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)
