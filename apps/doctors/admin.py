
from django.contrib import admin

from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "department",
        "specialization",
        "experience_years",
        "consultation_fee",
        "is_available",
    )

    list_filter = (
        "department",
        "is_available",
    )

    search_fields = (
        "user__full_name",
        "user__email",
        "user__phone",
        "specialization",
    )

    list_select_related = (
        "user",
        "department",
    )
