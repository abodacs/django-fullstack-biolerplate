from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel


class Project(IndexedTimeStampedModel):
    title = models.CharField(verbose_name=_("Project title"), max_length=128)
    project_class = models.ForeignKey(
        "meta.ProjectClass", verbose_name=_("Project Class"), on_delete=models.CASCADE,
    )
    case_types = models.ManyToManyField("meta.CaseType", related_name="project_case_types")
    envoys = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="project_envoys")
    start_date = models.DateField(verbose_name=_("Start Date"), null=True)
    end_date = models.DateField(verbose_name=_("End Date"), null=True)
    description = models.TextField(
        verbose_name=_("Project description"),
        blank=True,
        null=False,
        help_text=_("Long description for the Project"),
    )

    def clean(self):
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError(_("Project start date can be less than end date."))

    class Meta:
        app_label = "projects"
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title or "Project"


class Case(IndexedTimeStampedModel):
    name = models.CharField(_("Name"), max_length=128)
    code = models.SlugField(_("Code"), max_length=128, unique=True,)
    famous_name = models.CharField(_("Famous Name"), max_length=128, blank=True, null=True)
    mobile = models.CharField(_("Mobile"), max_length=32, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=150, blank=True, null=True)
    national_id = models.CharField(
        max_length=32, verbose_name=_("National ID"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=False,
        help_text=_("Long description for the Case"),
    )
    types = models.ManyToManyField("meta.CaseType", related_name="case_types")
    problems = models.ManyToManyField("meta.Problem", related_name="case_problems")
    envoy = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("Case Envoy"), on_delete=models.CASCADE,
    )

    class Meta:
        app_label = "projects"
        verbose_name = _("Case")
        verbose_name_plural = _("Cases")

    def __str__(self):
        return self.name or "Case"
