import importlib
from django.contrib import admin
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class CharactersAdmin(admin.ModelAdmin):
    list_filter = ('class_field',)
    sortable_by = ('name', 'base_level', 'job_level')
    list_display = ('name', 'class_name', 'base_level', 'job_level')


admin.site.register(models.Char, CharactersAdmin)
