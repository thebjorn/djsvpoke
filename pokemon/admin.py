from django.contrib import admin
from .models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['pokemon_id', 'name', 'types', 'height', 'weight', 'family']
    list_filter = ['family']
    search_fields = ['name', 'types', 'family']
    ordering = ['pokemon_id']
