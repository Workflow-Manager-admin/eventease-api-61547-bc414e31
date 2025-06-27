from django.contrib import admin
from .models import Event


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'start_time', 'end_time', 'created_at')
    search_fields = ('name', 'location')
    ordering = ('-start_time',)
