from django.urls import path
from django.http import JsonResponse

app_name = "platform_accounts"

urlpatterns = [
    path("", lambda request: JsonResponse({"service": "platform", "status": "foundation-ready"}), name="index"),
]
