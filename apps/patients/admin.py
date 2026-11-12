from django.contrib import admin
from .models import PatientProfile


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "gender",
        "blood_group",
        "date_of_birth",
    )

    search_fields = (
        "user__full_name",
        "user__email",
        "user__phone",
    )

    list_filter = (
        "gender",
        "blood_group",
    )
