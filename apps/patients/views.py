from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import PatientProfile
from .forms import PatientProfileForm


@login_required
def profile_view(request):
    profile = PatientProfile.objects.get(user=request.user)

    return render(
        request,
        "patients/profile.html",
        {"profile": profile}
    )


@login_required
def profile_edit_view(request):
    profile = PatientProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = PatientProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("patients:profile")

    else:
        form = PatientProfileForm(instance=profile)

    return render(
        request,
        "patients/profile_edit.html",
        {"form": form}
    )
