from django.contrib import admin

# Register your models here.
from results.models import Result, GoalsScored, GoalsConceded

admin.site.register(Result)
admin.site.register(GoalsScored)
admin.site.register(GoalsConceded)
