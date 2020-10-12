from django.contrib import admin

# Register your models here.
from .models import User, Player, Coach, Contract, Contact

admin.site.register(User)
admin.site.register(Player)


admin.site.register(Coach)
admin.site.register(Contract)
admin.site.register(Contact)


