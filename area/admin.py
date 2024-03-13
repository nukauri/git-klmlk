from django.contrib import admin

# Register your models here.

from .models import  Area, Address


admin.site.register(Area)
admin.site.register(Address)

