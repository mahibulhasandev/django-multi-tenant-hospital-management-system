from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok", "service": "multi-tenant-hms"})

urlpatterns = [
    path("health/", health_check, name="health"),
    path("admin/", admin.site.urls),
    path("platform/", include(("apps.platform_apps.platform_accounts.urls", "platform_accounts"), namespace="platform_accounts")),
]
