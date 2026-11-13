from django.apps import AppConfig

class HospitalAccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.hospital_apps.accounts"
    label = "hospital_accounts"
    verbose_name = "Hospital Memberships"
