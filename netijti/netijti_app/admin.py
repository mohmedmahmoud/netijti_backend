from django.contrib import admin

# Register your models here.

from .models import Result,Sector

admin.site.register(Result)
admin.site.register(Sector)
