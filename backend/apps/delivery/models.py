from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common import JobStatus
from common.models import IndexedTimeStampedModel, Job


class PatchQueryset(models.QuerySet):
    def ready(self):
        return self.filter(job__status=JobStatus.SUCCESS)


class Patch(Job):
    project = models.ForeignKey(
        "projects.Project", verbose_name=_("Project"), on_delete=models.CASCADE,
    )
    date = models.DateField(_("date"), db_index=True)
    closed = models.BooleanField(_("Closed"), default=False, db_index=True)

    class Meta:
        app_label = "delivery"
        verbose_name = _("Patch")
        verbose_name_plural = _("Patches")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.project}, {self.date}"


class Confirmation(IndexedTimeStampedModel):
    project = models.ForeignKey(
        "projects.Project", verbose_name=_("Project"), on_delete=models.CASCADE,
    )
    case = models.ForeignKey("projects.Case", verbose_name=_("Case"), on_delete=models.CASCADE,)
    envoy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Case Envoy"),
        on_delete=models.CASCADE,
        related_name="confirmations",
    )

    patch = models.ForeignKey("Patch", verbose_name=_("Patch"), on_delete=models.CASCADE,)
    delivered = models.BooleanField(verbose_name=_("Delivered?"), null=True)

    class Meta:
        app_label = "delivery"
        verbose_name = _("Confirmation")
        verbose_name_plural = _("Confirmations")
        ordering = ["delivered"]
