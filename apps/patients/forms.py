from datetime import date
from django import forms
from .models import PatientProfile


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile

        fields = [
            "date_of_birth",
            "gender",
            "blood_group",
            "address",
            "profile_picture",
            "emergency_contact_name",
            "emergency_contact_phone",
        ]

        widgets = {
            "date_of_birth": forms.DateInput(attrs={
                "type": "date",
                "min": "1900-01-01",
                "max": date.today().isoformat(),
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }),

            "gender": forms.Select(attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 bg-white focus:outline-none focus:ring-2 focus:ring-teal-500",
            }),

            "blood_group": forms.Select(
                choices=[
                    ("", "Select Blood Group"),
                    ("A+", "A+"),
                    ("A-", "A-"),
                    ("B+", "B+"),
                    ("B-", "B-"),
                    ("AB+", "AB+"),
                    ("AB-", "AB-"),
                    ("O+", "O+"),
                    ("O-", "O-"),
                ],
                attrs={
                    "class": "w-full rounded-xl border border-slate-300 px-4 py-3 bg-white focus:outline-none focus:ring-2 focus:ring-teal-500",
                }
            ),

            "address": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Enter your full address",
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }),

            "profile_picture": forms.ClearableFileInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 p-3 bg-white",
            }),

            "emergency_contact_name": forms.TextInput(attrs={
                "placeholder": "Emergency contact name",
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }),

            "emergency_contact_phone": forms.TextInput(attrs={
                "placeholder": "Emergency contact phone",
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")

        if dob:
            if dob > date.today():
                raise forms.ValidationError(
                    "Date of birth cannot be in the future."
                )

            if dob.year < 1900:
                raise forms.ValidationError(
                    "Please enter a valid date of birth."
                )

        return dob
