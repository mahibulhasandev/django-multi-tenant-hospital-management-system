from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Define this module's models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    class Role(models.TextChoices):
        HOSPITAL_ADMIN = "HOSPITAL_ADMIN", "Hospital Admin"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"
        STAFF = "STAFF", "Staff"
        PATIENT = "PATIENT", "Patient"
        LABORATORY_TECHNICIAN = "LABORATORY_TECHNICIAN", "Laboratory Technician"
        PHARMACIST = "PHARMACIST", "Pharmacist"
        
    email = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    
    full_name = models.CharField(max_length=150)

    role = models.CharField(max_length=30, choices=Role.choices, default=Role.PATIENT)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]


    def __str__(self):
        return self.full_name



class StaffRegistrationRequest(models.Model):

    class RequestedRole(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"
        STAFF = "STAFF", "Staff"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="staff_registration_request"
    )

    requested_role = models.CharField(
        max_length=30,
        choices=RequestedRole.choices
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_staff_requests"
    )

    reviewed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    rejection_reason = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Staff Registration Request"
        verbose_name_plural = "Staff Registration Requests"

    def __str__(self):
        return (
            f"{self.user.full_name} - "
            f"{self.get_requested_role_display()} - "
            f"{self.get_status_display()}"
        )

   