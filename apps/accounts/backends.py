from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        identifier = username or kwargs.get("email") or kwargs.get("phone")

        if not identifier or not password:
            return None
        
        User = get_user_model()
        user = User.objects.filter(Q(email__iexact=identifier) | Q(phone=identifier)).first()

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user



        return None