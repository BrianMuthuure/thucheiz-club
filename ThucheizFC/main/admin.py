from django.contrib import admin

# Register your models here.
from .models import User, Player, Coach, PlayerContract, Contact

admin.site.register(User)
admin.site.register(Coach)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['jersey_no', 'position', 'image', 'available', 'goals', 'appearances']


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerContract)
admin.site.register(Contact)