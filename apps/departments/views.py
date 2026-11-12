from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from .models import Department
from .forms import DepartmentForm


def hospital_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")

        if request.user.role != "HOSPITAL_ADMIN":
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


@login_required
@hospital_admin_required
def department_list(request):
    departments = Department.objects.all().order_by("name")

    return render(
        request,
        "departments/department_list.html",
        {"departments": departments}
    )


@login_required
@hospital_admin_required
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Department created successfully.")
            return redirect("departments:department_list")

    else:
        form = DepartmentForm()

    return render(
        request,
        "departments/department_form.html",
        {"form": form, "title": "Create Department"}
    )


@login_required
@hospital_admin_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)

    return render(
        request,
        "departments/department_detail.html",
        {"department": department}
    )


@login_required
@hospital_admin_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        form = DepartmentForm(
            request.POST,
            request.FILES,
            instance=department
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully.")
            return redirect("departments:department_list")

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "departments/department_form.html",
        {"form": form, "title": "Update Department"}
    )


@login_required
@hospital_admin_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        department.delete()
        messages.success(request, "Department deleted successfully.")
        return redirect("departments:department_list")

    return render(
        request,
        "departments/department_detail.html",
        {"department": department, "confirm_delete": True}
    )
