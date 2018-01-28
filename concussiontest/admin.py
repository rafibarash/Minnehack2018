from django.contrib import admin
from .models import Athlete

class AthleteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'base_time', 'new_time_1', 'new_time_2')
    search_fields = ['name']
admin.site.register(Athlete, AthleteAdmin)
