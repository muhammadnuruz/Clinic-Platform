from django.contrib import admin

from apps.analyses.models import Analyses


class AnalysesAdmin(admin.ModelAdmin):
    list_display = ('analyse_id', 'created_at')
    ordering = ('analyse_id',)


admin.site.register(Analyses, AnalysesAdmin)
