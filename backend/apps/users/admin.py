from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from apps.users.forms import UserChangeForm, UserCreationForm


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
    list_display = [
        "username",
        "name",
        "type",
    ]
    search_fields = ["name"]
