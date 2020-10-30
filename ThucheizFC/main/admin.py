from django.contrib import admin

# Register your models here.
from .models import User, Player, Coach, Contract, Contact, Injury, CoachContract, DeletedPlayer, Picture

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Injury)
admin.site.register(Picture)


admin.site.register(Coach)
admin.site.register(Contract)
admin.site.register(CoachContract)
admin.site.register(Contact)
admin.site.register(DeletedPlayer)


