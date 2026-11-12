from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.core.exceptions import PermissionDenied
from .forms import LoginForm, PatientRegistrationForm
from django.db import transaction
from .forms import StaffRegistrationForm
# from .models import StaffRegistrationRequest
from .models import User, StaffRegistrationRequest


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            identifier = form.cleaned_data["identifier"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=identifier,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("accounts:dashboard")

            messages.error(request, "Invalid email/phone or password.")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("accounts:login")

    return redirect("accounts:dashboard")


@login_required
def dashboard_view(request):

    dashboards = {
        "HOSPITAL_ADMIN": "dashboards/admin.html",
        "DOCTOR": "dashboards/doctor.html",
        "NURSE": "dashboards/nurse.html",
        "RECEPTIONIST": "dashboards/receptionist.html",
        "STAFF": "dashboards/staff.html",
        "PATIENT": "dashboards/patient.html",
        "LABORATORY_TECHNICIAN": "dashboards/laboratory.html",
        "PHARMACIST": "dashboards/pharmacy.html",
    }

    template = dashboards.get(request.user.role)

    if not template:
        raise PermissionDenied("You don't have dashboard access.")

    return render(request, template)


def register_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your account has been created successfully. Please login."
            )

            return redirect("accounts:login")

    else:
        form = PatientRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def staff_register_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)

        if form.is_valid():

            with transaction.atomic():

                user = form.save(commit=False)

                user.role = User.Role.PATIENT
                user.is_active = False

                user.save()

                StaffRegistrationRequest.objects.create(
                    user=user,
                    requested_role=form.cleaned_data["requested_role"],
                    department=form.cleaned_data.get("department"),
                    specialization=form.cleaned_data.get("specialization") or "",
                    qualification=form.cleaned_data.get("qualification") or "",
                    experience_years=form.cleaned_data.get("experience_years"),
                    consultation_fee=form.cleaned_data.get("consultation_fee"),
                )

            messages.success(
                request,
                "Your registration request has been submitted. "
                "Please wait for Hospital Admin approval."
            )

            return redirect("accounts:login")

    else:
        form = StaffRegistrationForm()

    return render(
        request,
        "accounts/staff_register.html",
        {"form": form}
    )


