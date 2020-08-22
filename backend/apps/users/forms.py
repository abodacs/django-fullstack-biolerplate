from django import forms as django_forms
from django.contrib.auth import forms, get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Envoy


User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class EnvoyChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Envoy
        fields = "__all__"


class UserCreationForm(django_forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "duplicate_username": _("This username has already been taken."),
    }
    password1 = django_forms.CharField(
        label=_("Password"),
        strip=False,
        widget=django_forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = django_forms.CharField(
        label=_("Password confirmation"),
        widget=django_forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs["autofocus"] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"], code="password_mismatch",
            )
        return password2

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"
        field_classes = {"username": forms.UsernameField}
