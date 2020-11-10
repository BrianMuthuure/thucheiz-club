import django_filters
from django_filters import DateRangeFilter, CharFilter

from .models import *


class DeletedPlayerFilter(django_filters.FilterSet):
    date_range = DateRangeFilter(field_name='date')

    class Meta:
        model = DeletedPlayer
        fields = '__all__'
        exclude = ['player', 'date']


class InjuryFilter(django_filters.FilterSet):
    date_range = DateRangeFilter(field_name='date_added')

    class Meta:
        model = Injury
        fields = '__all__'
        exclude = ['player', 'date_added']
