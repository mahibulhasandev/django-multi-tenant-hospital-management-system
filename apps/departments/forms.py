from django import forms

from .models import Department
from apps.doctors.models import DoctorProfile


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            "name",
            "description",
            "head_of_department",
            "image",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields["head_of_department"].queryset = (
                DoctorProfile.objects.filter(
                    department=self.instance
                )
            )
        else:
            self.fields["head_of_department"].queryset = (
                DoctorProfile.objects.none()
            )
