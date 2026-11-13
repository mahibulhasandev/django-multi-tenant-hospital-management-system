import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import PlatformUserManager

class PlatformUser(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=160)
    objects = PlatformUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = "Platform user"
        verbose_name_plural = "Platform users"

    def __str__(self):
        return self.email
