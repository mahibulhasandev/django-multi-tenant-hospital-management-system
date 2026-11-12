from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Department(models.Model):

    name = models.CharField(max_length=150, unique=True)

    slug = models.SlugField(max_length=170, unique=True, blank=True)

    description = models.TextField()

    head_of_department = models.ForeignKey(
        "doctors.DoctorProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="headed_departments"
    )

    image = models.ImageField(
        upload_to="departments/",
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.head_of_department and self.head_of_department.department_id != self.pk:
            raise ValidationError({
                "head_of_department": (
                    "The selected doctor must belong to this department."
                )
            })
