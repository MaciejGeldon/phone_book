from django.contrib import admin

from core.models import Country, Entry


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'prefix']


@admin.register(Entry)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'full_number', 'description']
