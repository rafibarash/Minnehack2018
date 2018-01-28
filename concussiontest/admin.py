from django.contrib import admin
from .models import Athlete

class AthleteAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'base_time', 'base_errors')
    search_fields = ['first', 'last']
admin.site.register(Athlete, AthleteAdmin)
