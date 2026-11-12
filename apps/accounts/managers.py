from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email=None, phone=None, password=None, **extra_fields):
        email = self.normalize_email(email) if email else None
        phone = phone.strip() if phone else None
        
        if not email and not phone:
            raise ValueError("Email or phone number is required..")
        
        user = self.model(email=email, phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    
    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, phone, password, **extra_fields)

    def create_superuser(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email, phone, password, **extra_fields)