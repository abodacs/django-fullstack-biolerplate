from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from apps.users.forms import EnvoyChangeForm, UserChangeForm, UserCreationForm

from .models import Envoy


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "type",)}),
        (_("Permissions"), {"fields": ("is_active", "is_superuser",),}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_filter = (
        "is_active",
        "type",
    )
    list_display = [
        "username",
        "name",
        "type",
    ]
    search_fields = ["name"]


@admin.register(Envoy)
class EnvoyAdmin(auth_admin.UserAdmin):
    form = EnvoyChangeForm
    add_form = UserCreationForm
    list_filter = ("is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "type", "area_in_charge", "mobile",)}),
        (_("Permissions"), {"fields": ("is_active",)}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_display = [
        "username",
        "name",
        "type",
        "mobile",
    ]
    search_fields = ["name"]
