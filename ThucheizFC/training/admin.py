from django.contrib import admin

# Register your models here.
from training.models import TrainingSession


class TrainingSessionAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_filter = ('status',)
    filter_vertical = ('player', 'coach')


admin.site.register(TrainingSession, TrainingSessionAdmin)