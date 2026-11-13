from django.contrib import admin
from .models import TenantDatabase

@admin.register(TenantDatabase)
class TenantDatabaseAdmin(admin.ModelAdmin):
    list_display = ("hospital", "database_name", "status", "schema_version", "last_migrated_at")
    list_filter = ("status",)
    search_fields = ("hospital__name", "database_name")
    readonly_fields = ("created_at", "last_migrated_at")
