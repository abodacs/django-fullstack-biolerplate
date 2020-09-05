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
    mobile = models.CharField(_("Mobile"), max_length=32, blank=True, null=True)
    areas_in_charge = models.ManyToManyField(
        "meta.Area", verbose_name=_("Area in Charge"), related_name="envoy_areas_in_charge"
    )
    is_staff = models.BooleanField(default=False, help_text=_("Staff"))
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

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username


class EnvoyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ENVOY)


class Envoy(User):
    base_type = User.Types.ENVOY
    objects = EnvoyManager()

    class Meta:
        proxy = True
