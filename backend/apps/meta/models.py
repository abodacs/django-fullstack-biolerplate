from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel


class ProjectClass(IndexedTimeStampedModel):
    name = models.CharField(_("Name"), max_length=128)
    slug = models.SlugField(_("Slug"), max_length=128, unique=True, editable=False,)
    YEARLY, SEASONAL, MONTHLY, MonthlyHijri, Daily = (
        "Yearly",
        "Seasonal",
        "Monthly",
        "Monthly-Hijri",
        "Daily",
    )
    TYPE_CHOICES = (
        (YEARLY, _("Seasonal - Occur  each Year.")),
        # (SEASONAL, _("Seasonal - Occur on particular season of the year.")),
        (MonthlyHijri, _("Monthly - repeated at each Hijri Monthly")),
        (MONTHLY, _("Monthly - repeated Monthly")),
        (Daily, _("Daily - repeated Daily")),
    )
    type = models.CharField(_("Status"), max_length=128, default=Daily, choices=TYPE_CHOICES)

    @property
    def check_every_num_days(self):
        """convert type to num_days to check"""
        # TODO: fix this naive solve
        num_days = 0
        if self.type == self.YEARLY:
            num_days = 365
        elif self.type == self.MONTHLY:
            num_days = 30
        elif self.type == self.MonthlyHijri:
            num_days = 28
        return num_days

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("name",)
        app_label = "meta"
        verbose_name = _("ProjectClass")
        verbose_name_plural = _("ProjectClasses")

    def __str__(self):
        return self.name


class Problem(IndexedTimeStampedModel):
    name = models.CharField(_("Name"), max_length=128)
    order = models.PositiveSmallIntegerField(
        verbose_name=_("order the field in the app"), default=1,
    )

    class Meta:
        ordering = (
            "order",
            "name",
        )
        app_label = "meta"
        verbose_name = _("Problem")
        verbose_name_plural = _("Problems")

    def __str__(self):
        return self.name


class CaseType(IndexedTimeStampedModel):
    name = models.CharField(_("Name"), max_length=128)
    order = models.PositiveSmallIntegerField(
        verbose_name=_("order the field in the app"), default=1,
    )

    class Meta:
        ordering = (
            "order",
            "name",
        )
        app_label = "meta"
        verbose_name = _("CaseType")
        verbose_name_plural = _("CaseTypes")

    def __str__(self):
        return self.name


class Area(IndexedTimeStampedModel):
    name = models.CharField(_("Name"), max_length=128)
    order = models.PositiveSmallIntegerField(
        verbose_name=_("order the field in the app"), default=1,
    )

    class Meta:
        ordering = (
            "order",
            "name",
        )
        app_label = "meta"
        verbose_name = _("Area")
        verbose_name_plural = _("Area")

    def __str__(self):
        return self.name
