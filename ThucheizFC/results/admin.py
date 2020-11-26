from django.contrib import admin

# Register your models here.
from results.models import Result, GoalsScored, GoalsConceded

admin.site.register(Result)


class GoalsScoredAdmin(admin.ModelAdmin):
    list_display = ('result', 'player', 'minute')
    list_filter = ('result',)


admin.site.register(GoalsScored, GoalsScoredAdmin)


class GoalsConcededAdmin(admin.ModelAdmin):
    list_display = ('result', 'scorer', 'minute')
    list_filter = ('result',)


admin.site.register(GoalsConceded, GoalsConcededAdmin)