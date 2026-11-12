from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    
    list_display = (
        "id",
        "email",
        "phone",
        "full_name",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "email",
        "phone",
        "full_name",
    )

    ordering = ("id",)

    fieldsets = (
        ("Account Information", {
            "fields": ("email", "phone", "password")
        }),
        ("Personal Information", {
            "fields": ("full_name", "role")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    readonly_fields = ("last_login", "date_joined")

    add_fieldsets = (
        ("Create New User", {
            "classes": ("wide",),
            "fields": (
                "email",
                "phone",
                "full_name",
                "role",
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
