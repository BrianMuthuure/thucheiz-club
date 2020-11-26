from django.contrib import admin

# Register your models here.
from .models import User, Player, Coach, Contract, Contact, Injury, CoachContract, Inaccessible, Picture, PlayerJersey


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_admin', 'is_player', 'is_coach')
    list_display_links = ('first_name', 'last_name', 'email')
    list_per_page = 7
    search_fields = ('username', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'jersey_no', 'country', 'dob', 'age',  'available', 'injured')
    list_per_page = 7
    list_filter = ('country', 'position', 'age', 'available', 'injured')


admin.site.register(Player, PlayerAdmin)

admin.site.register(Injury)
admin.site.register(Picture)
admin.site.register(PlayerJersey)


class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'nationality', 'age', 'trophies', 'games', 'wins', 'losses')
    list_filter = ('title', 'nationality', 'trophies')


admin.site.register(Coach, CoachAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_per_page = 7


admin.site.register(Contract, ContractAdmin)
admin.site.register(CoachContract)
admin.site.register(Contact)


class InaccessibleAdmin(admin.ModelAdmin):
    list_display = ('player', 'status', 'date')
    list_filter = ('status', 'date')


admin.site.register(Inaccessible, InaccessibleAdmin)


