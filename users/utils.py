from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    
    def _create_user(self, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):
        
        now = timezone.now()

        if not email:
            raise ValueError('Email Obrigatório!')

        email = self.normalize_email(email)

        user = self.model(
            email = email,
            first_name = first_name, 
            last_name = last_name,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, first_name, last_name, password, True, False, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        return self._create_user(email, first_name, last_name, password, True, True, **extra_fields)