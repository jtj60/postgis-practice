from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import WorldBorder

# Register your models here.
admin.site.register(WorldBorder, GISModelAdmin)