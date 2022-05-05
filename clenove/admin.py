from django.contrib import admin

# Register your models here.

from .models import Skaut, Oddil, AdresaKlubovny, Bobrik

# @admin.register(Skaut)
# dekorator

class SkautAdmin(admin.ModelAdmin):
    # readonly_fields = ["slug"]
    prepopulated_fields = {"slug" : ("prezdivka",)}
    list_display = ["jmeno", "prezdivka", "splneno", "vek", "oddil"]
    list_filter = ["splneno", "vek", "oddil"]

class OddilAdmin(admin.ModelAdmin):
    list_display = ["jmeno", "heslo", "seznam_skautu"]

@admin.register(AdresaKlubovny)
class AdresaKlubovnyAdmin(admin.ModelAdmin):
    list_disply = ["ulice", "cislo popisne"]

@admin.register(Bobrik)
class BobrikAdmin(admin.ModelAdmin):
    list_display = ["nazev", "barva"]

admin.site.register(Skaut, SkautAdmin)
admin.site.register(Oddil, OddilAdmin)