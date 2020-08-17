from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    user_name = models.CharField(max_length=255, unique=True)
    name = models.CharField(verbose_name='name', max_length=64, default='name')
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin " "site.")
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "user_name"

    def get_full_name(self):
        return self.user_name

    def get_short_name(self):
        return self.user_name

    def __str__(self):
        return str(self.name or self.user_name)
