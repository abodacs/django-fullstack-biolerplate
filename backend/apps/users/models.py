from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    class Types(models.TextChoices):
        MANAGER = "MANAGER", _("Manager")
        ENVOY = "ENVOY", _("Envoy")

    base_type = Types.ENVOY
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(verbose_name="name", max_length=255, default="name")
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
        verbose_name = "User"
        verbose_name_plural = "Users"

    # Fields settings
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "username",
    ]

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return str(self.username or self.name or "")
