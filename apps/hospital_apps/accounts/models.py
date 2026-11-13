import uuid
from django.db import models

class HospitalMembership(models.Model):
    class Status(models.TextChoices):
        INVITED = "invited", "Invited"
        ACTIVE = "active", "Active"
        SUSPENDED = "suspended", "Suspended"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # UUID of the central PlatformUser. Deliberately no cross-database FK.
    global_user_id = models.UUIDField(db_index=True)
    role = models.CharField(max_length=40)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.INVITED)
    joined_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("global_user_id",), name="unique_global_user_per_hospital")
        ]
        indexes = [models.Index(fields=("role", "status"))]

    def __str__(self):
        return f"{self.global_user_id} - {self.role}"
