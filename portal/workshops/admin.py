from datetime import timedelta

from django.contrib import admin

from .models import Workshop, Session, Environment

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "url"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ["name", "workshop_name", "duration", "capacity",
            "available_sessions_count", "allocated_sessions_count"]

    readonly_fields = ["name", "workshop", "initial", "tally", "resource"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class SessionAdmin(admin.ModelAdmin):
    list_display = ["name", "workshop_name", "is_available", "is_allocated",
            "is_stopped", "remaining_time_as_string"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    actions = ["extend_sessions_10m", "extend_sessions_30m",
            "extend_sessions_60m"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def extend_sessions(self, request, queryset, minutes):
        for session in queryset:
            if session.is_allocated() and session.expires:
                session.expires += timedelta(minutes=minutes)
                session.save()

    def extend_sessions_10m(self, request, queryset):
        self.extend_sessions(request, queryset, 10)

    extend_sessions_10m.short_description = "Extend Sessions (10m)"

    def extend_sessions_30m(self, request, queryset):
        self.extend_sessions(request, queryset, 30)

    extend_sessions_30m.short_description = "Extend Sessions (30m)"

    def extend_sessions_60m(self, request, queryset):
        self.extend_sessions(request, queryset, 60)

    extend_sessions_60m.short_description = "Extend Sessions (60m)"

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Session, SessionAdmin)
