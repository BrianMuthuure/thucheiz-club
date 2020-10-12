from django.contrib import admin

# Register your models here.
from injury.models import Injury, CheckOut

admin.site.register(Injury)
admin.site.register(CheckOut)