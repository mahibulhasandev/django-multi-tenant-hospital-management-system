
from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [

    # Doctor Management
    path("", views.doctor_list, name="doctor_list"),
    path("create/", views.doctor_create, name="doctor_create"),
    path("<int:pk>/", views.doctor_detail, name="doctor_detail"),
    path("<int:pk>/edit/", views.doctor_update, name="doctor_update"),
    path("<int:pk>/delete/", views.doctor_delete, name="doctor_delete"),

    # Doctor Schedule Management
    path("schedules/", views.schedule_list, name="schedule_list"),
    path("schedules/create/", views.schedule_create, name="schedule_create"),
    path("schedules/<int:pk>/", views.schedule_detail, name="schedule_detail"),
    path("schedules/<int:pk>/edit/", views.schedule_update, name="schedule_update"),
    path("schedules/<int:pk>/delete/", views.schedule_delete, name="schedule_delete"),
]
