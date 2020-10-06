from django.contrib import admin

# Register your models here.
from results.models import Result, ClubGoal, OpponentGoal

admin.site.register(Result)
admin.site.register(ClubGoal)
admin.site.register(OpponentGoal)
