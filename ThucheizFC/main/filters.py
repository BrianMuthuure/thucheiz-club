import django_filters

from .models import *


class PlayerFilter(django_filters.FilterSet):
    class Meta:
        model = Player
        fields = '__all__'