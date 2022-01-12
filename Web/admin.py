from django.contrib import admin
from .models import Command, BasicConfiguration


# Register your models here.
class CommandAdmin(admin.ModelAdmin):
    list_display = ['command', 'delay']


class BasicConfigurationAdmin(admin.ModelAdmin):
    list_display = ['stationId', 'serverUrl']


admin.site.register(Command, CommandAdmin)
admin.site.register(BasicConfiguration, BasicConfigurationAdmin)
