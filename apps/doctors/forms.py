from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from apps.departments.models import Department
from .models import DoctorProfile, DoctorSchedule

User = get_user_model()


class DoctorCreationForm(forms.ModelForm):

    full_name = forms.CharField(max_length=150)

    email = forms.EmailField(required=False)

    phone = forms.CharField(max_length=20, required=False)

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = DoctorProfile
        fields = [
            "department",
            "specialization",
            "qualification",
            "experience_years",
            "consultation_fee",
            "is_available",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if phone and User.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                "This phone number is already registered.")

        return phone

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if not email and not phone:
            raise forms.ValidationError(
                "Email or phone number is required."
            )

        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    "confirm_password",
                    "Passwords do not match."
                )
            else:
                try:
                    validate_password(password)
                except forms.ValidationError as error:
                    self.add_error("password", error)

        return cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        doctor_profile = super().save(commit=False)

        user = User.objects.create_user(
            email=self.cleaned_data["email"] or None,
            phone=self.cleaned_data["phone"] or None,
            password=self.cleaned_data["password"],
            full_name=self.cleaned_data["full_name"],
            role=User.Role.DOCTOR,
        )

        doctor_profile.user = user

        if commit:
            doctor_profile.save()

        return doctor_profile


class DoctorUpdateForm(forms.ModelForm):

    class Meta:
        model = DoctorProfile
        fields = [
            "department",
            "specialization",
            "qualification",
            "experience_years",
            "consultation_fee",
            "is_available",
        ]



class DoctorScheduleForm(forms.ModelForm):

    class Meta:
        model = DoctorSchedule

        fields = [
            "doctor",
            "day_of_week",
            "start_time",
            "end_time",
            "slot_duration",
            "break_start",
            "break_end",
            "is_available",
        ]

        widgets = {
            "doctor": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "day_of_week": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "start_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "end_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "slot_duration": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "break_start": forms.TimeInput(attrs={
                "type": "time",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "break_end": forms.TimeInput(attrs={
                "type": "time",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
            }),

            "is_available": forms.CheckboxInput(attrs={
                "class": "rounded border-gray-300 text-teal-600"
            }),
        }

        labels = {
            "doctor": "Select Doctor",
            "day_of_week": "Working Day",
            "start_time": "Start Time",
            "end_time": "End Time",
            "slot_duration": "Appointment Duration",
            "break_start": "Break Start",
            "break_end": "Break End",
            "is_active": "Available",
        }

        help_texts = {
            "slot_duration": "Select 15, 30 or 45 minutes.",
            "is_active": "Uncheck if the doctor is unavailable.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["doctor"].queryset = (
            DoctorProfile.objects
            .filter(user__is_active=True)
            .select_related("user", "department")
        )
