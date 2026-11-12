
from django.db import models
from django.conf import settings


class PatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )

    date_of_birth = models.DateField(null=True, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=[
            ("MALE", "Male"),
            ("FEMALE", "Female"),
            ("OTHER", "Other"),
        ],
        blank=True
    )

    blood_group = models.CharField(
        max_length=5,
        blank=True
    )

    address = models.TextField(blank=True)

    profile_picture = models.ImageField(
        upload_to="patients/profile/",
        null=True,
        blank=True
    )

    emergency_contact_name = models.CharField(
        max_length=150,
        blank=True
    )

    emergency_contact_phone = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.user.full_name
