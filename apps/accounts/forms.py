from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, StaffRegistrationRequest
from apps.departments.models import Department

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "phone",
            "full_name",
            "role",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "phone",
            "full_name",
            "role",
        )


class LoginForm(forms.Form):
    identifier = forms.CharField(
        label="Email or Phone Number",
        max_length=254,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter email or phone number",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            "autocomplete": "username",
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter your password",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            "autocomplete": "current-password",
        })
    )


class PatientRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "phone",
        )

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if not email and not phone:
            raise forms.ValidationError(
                "Email or phone number is required."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = User.Role.PATIENT

        if commit:
            user.save()

        return user
    
    widgets = {
        "full_name": forms.TextInput(attrs={
            "class": "w-full block bg-transparent outline-none text-base py-1",
            "placeholder": "Enter your full name",
        }),

        "email": forms.EmailInput(attrs={
            "class": "w-full block bg-transparent outline-none text-base py-1",
            "placeholder": "Enter your email address",
        }),

        "phone": forms.TextInput(attrs={
            "class": "w-full block bg-transparent outline-none text-base py-1",
            "placeholder": "Enter your phone number",
        }),
    }


class StaffRegistrationForm(UserCreationForm):

    requested_role = forms.ChoiceField(
        choices=StaffRegistrationRequest.RequestedRole.choices,
        label="Select Your Role"
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        empty_label="Select Department"
    )

    specialization = forms.CharField(
        max_length=150,
        required=False
    )

    qualification = forms.CharField(
        max_length=255,
        required=False
    )

    experience_years = forms.IntegerField(
        required=False,
        min_value=0
    )

    consultation_fee = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        min_value=0
    )

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "phone",
        )

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if not email and not phone:
            raise forms.ValidationError(
                "Email or phone number is required."
            )

        role = cleaned_data.get("requested_role")

        if role == StaffRegistrationRequest.RequestedRole.DOCTOR:

            required_fields = (
                "department",
                "specialization",
                "qualification",
                "experience_years",
                "consultation_fee",
            )

            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(
                        field,
                        "This field is required for Doctor registration."
                    )

        return cleaned_data
