from django.contrib import admin

from apps.analysis_type.models import Types

class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ru_name', 'price', 'to_be_ready', 'created_at')
    ordering = ('name', 'ru_name', 'to_be_ready', 'created_at')


admin.site.register(Types, TypesAdmin)
