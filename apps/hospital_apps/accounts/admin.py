from django.contrib import admin
from .models import HospitalMembership

@admin.register(HospitalMembership)
class HospitalMembershipAdmin(admin.ModelAdmin):
    list_display = ("global_user_id", "role", "status", "created_at")
    list_filter = ("role", "status")
    search_fields = ("global_user_id",)
