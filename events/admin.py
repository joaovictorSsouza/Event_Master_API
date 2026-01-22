from django.contrib import admin
from .models import Event, Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories',)
    search_fields = ('id',)

@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ('event_name', 'description',
                    'date', 'location', 'is_remote',
                    'capacity', 'price', 'category',)
    search_fields = ('event_name', 'date',)

