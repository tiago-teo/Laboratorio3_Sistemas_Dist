from django.contrib import admin

# Register your models here.

from .models import AppUser, Package

admin.site.register(AppUser)
admin.site.register(Package)
