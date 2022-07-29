from django.contrib import admin

from test_app.models import Durations


class DurationsAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'equipment',
        'start',
        'stop',
        'mode',
        'minutes',
    )
    search_fields = ('client',)


admin.site.register(Durations, DurationsAdmin)
