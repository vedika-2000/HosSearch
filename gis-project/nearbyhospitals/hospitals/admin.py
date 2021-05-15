from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
