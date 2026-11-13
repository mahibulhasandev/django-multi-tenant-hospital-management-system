from django.contrib import admin
from .models import Hospital, HospitalDomain

class HospitalDomainInline(admin.TabularInline):
    model = HospitalDomain
    extra = 0

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "slug", "registration_number")
    readonly_fields = ("id", "created_at", "updated_at")
    inlines = (HospitalDomainInline,)
