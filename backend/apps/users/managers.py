from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    @classmethod
    def normalize(cls, value):
        value = value
        return value.strip().lower()

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        user = self.model(
            username=self.normalize(username),
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_name=None, password=None, **extra_fields):
        is_staff = extra_fields.pop("is_staff", False)
        is_superuser = extra_fields.pop("is_superuser", False)
        if not password:
            raise ValueError("User must have a password")
        if not user_name:
            raise ValueError("User must have a user_name")
        return self._create_user(user_name, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, user_name, password, **extra_fields):
        return self._create_user(
            user_name, password, is_staff=True, is_superuser=True, **extra_fields
        )
