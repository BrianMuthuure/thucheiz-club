import django_filters
from django_filters import DateRangeFilter, CharFilter, DateFilter
from django import forms
from training.models import TrainingSession
from .models import *


class DeletedPlayerFilter(django_filters.FilterSet):
    date_range = DateRangeFilter(field_name='date')

    class Meta:
        model = Inaccessible
        fields = '__all__'
        exclude = ['player', 'date']


class InjuryFilter(django_filters.FilterSet):
    date_range = DateRangeFilter(field_name='date_added')

    class Meta:
        model = Injury
        fields = '__all__'
        exclude = ['player', 'date_added']


class SessionFilter(django_filters.FilterSet):
    From = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), field_name="date", lookup_expr='gt',
                      label='Date greater than')
    To = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), field_name="date", lookup_expr='lt',
                    label='Date less than')

    class Meta:
        model = TrainingSession
        fields = '__all__'
        exclude = ['player', 'coach', 'date', 'active']


class ContractFilter(django_filters.FilterSet):
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='icontains')
    From = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), field_name="end_date", lookup_expr='gt', label='End date greater than')
    To = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), field_name="end_date", lookup_expr='lt',  label='End date less than')

    class Meta:
        model = Contract
        fields = '__all__'
        exclude = ['player', 'buyout_clause', 'start_date', 'end_date', 'daily_pay']