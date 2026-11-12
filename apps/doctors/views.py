
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from .models import DoctorProfile, DoctorSchedule
from .forms import (
    DoctorCreationForm,
    DoctorUpdateForm,
    DoctorScheduleForm,
)


# Hospital Admin Permission
def hospital_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")

        if request.user.role != "HOSPITAL_ADMIN":
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================
# DOCTOR MANAGEMENT
# ==========================================

@login_required
@hospital_admin_required
def doctor_list(request):

    doctors = DoctorProfile.objects.select_related(
        "user", "department"
    ).all()

    return render(
        request,
        "doctors/doctor_list.html",
        {"doctors": doctors}
    )


@login_required
@hospital_admin_required
def doctor_create(request):

    if request.method == "POST":
        form = DoctorCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Doctor created successfully."
            )

            return redirect("doctors:doctor_list")

    else:
        form = DoctorCreationForm()

    return render(
        request,
        "doctors/doctor_form.html",
        {"form": form, "title": "Add Doctor"}
    )


@login_required
@hospital_admin_required
def doctor_detail(request, pk):

    doctor = get_object_or_404(
        DoctorProfile.objects.select_related("user", "department"),
        pk=pk
    )

    return render(
        request,
        "doctors/doctor_detail.html",
        {"doctor": doctor}
    )


@login_required
@hospital_admin_required
def doctor_update(request, pk):

    doctor = get_object_or_404(DoctorProfile, pk=pk)

    if request.method == "POST":
        form = DoctorUpdateForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Doctor updated successfully."
            )

            return redirect("doctors:doctor_list")

    else:
        form = DoctorUpdateForm(instance=doctor)

    return render(
        request,
        "doctors/doctor_form.html",
        {"form": form, "title": "Update Doctor"}
    )


@login_required
@hospital_admin_required
def doctor_delete(request, pk):

    doctor = get_object_or_404(DoctorProfile, pk=pk)

    if request.method == "POST":
        doctor.delete()

        messages.success(
            request,
            "Doctor profile deleted successfully."
        )

        return redirect("doctors:doctor_list")

    return render(
        request,
        "doctors/doctor_detail.html",
        {"doctor": doctor, "confirm_delete": True}
    )


# ==========================================
# DOCTOR SCHEDULE MANAGEMENT
# ==========================================

@login_required
@hospital_admin_required
def schedule_list(request):

    schedules = DoctorSchedule.objects.select_related(
        "doctor__user",
        "doctor__department"
    ).all()

    return render(
        request,
        "doctors/schedule_list.html",
        {"schedules": schedules}
    )


@login_required
@hospital_admin_required
def schedule_create(request):

    if request.method == "POST":
        form = DoctorScheduleForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Doctor schedule created successfully."
            )

            return redirect("doctors:schedule_list")

    else:
        form = DoctorScheduleForm()

    return render(
        request,
        "doctors/schedule_form.html",
        {"form": form, "title": "Create Doctor Schedule"}
    )


@login_required
@hospital_admin_required
def schedule_detail(request, pk):

    schedule = get_object_or_404(
        DoctorSchedule.objects.select_related(
            "doctor__user",
            "doctor__department"
        ),
        pk=pk
    )

    return render(
        request,
        "doctors/schedule_detail.html",
        {"schedule": schedule}
    )


@login_required
@hospital_admin_required
def schedule_update(request, pk):

    schedule = get_object_or_404(
        DoctorSchedule,
        pk=pk
    )

    if request.method == "POST":
        form = DoctorScheduleForm(
            request.POST,
            instance=schedule
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Doctor schedule updated successfully."
            )

            return redirect("doctors:schedule_list")

    else:
        form = DoctorScheduleForm(instance=schedule)

    return render(
        request,
        "doctors/schedule_form.html",
        {"form": form, "title": "Update Doctor Schedule"}
    )


@login_required
@hospital_admin_required
def schedule_delete(request, pk):

    schedule = get_object_or_404(
        DoctorSchedule,
        pk=pk
    )

    if request.method == "POST":
        schedule.delete()

        messages.success(
            request,
            "Doctor schedule deleted successfully."
        )

        return redirect("doctors:schedule_list")

    return render(
        request,
        "doctors/schedule_detail.html",
        {
            "schedule": schedule,
            "confirm_delete": True
        }
    )
