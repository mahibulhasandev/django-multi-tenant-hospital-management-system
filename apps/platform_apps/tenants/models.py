from django.db import models
from apps.platform_apps.hospitals.models import Hospital

class TenantDatabase(models.Model):
    class Status(models.TextChoices):
        NOT_CREATED = "not_created", "Not Created"
        READY = "ready", "Ready"
        ERROR = "error", "Error"

    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, related_name="tenant_database")
    database_name = models.CharField(max_length=63, unique=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NOT_CREATED)
    schema_version = models.CharField(max_length=40, blank=True)
    last_migrated_at = models.DateTimeField(null=True, blank=True)
    last_error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hospital.name} ({self.database_name})"
