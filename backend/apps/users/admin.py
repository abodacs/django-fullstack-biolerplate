from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.utils.translation import ugettext_lazy as _

from apps.projects.models import Case
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
        "show_cases_number",
    ]
    search_fields = ["name"]

    def show_cases_number(self, obj):
        url = reverse("admin:projects_case_changelist") + "?" + urlencode({"envoy_id": f"{obj.id}"})
        count = Case.objects.filter(envoy=obj).only("id").count()
        return format_html('<a href="{}">{} Cases</a>', url, count)

    show_cases_number.short_description = _("Cases Number")
