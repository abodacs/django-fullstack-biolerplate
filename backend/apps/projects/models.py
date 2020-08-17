from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import IndexedTimeStampedModel


class Project(models.Model, IndexedTimeStampedModel):
    name = models.CharField(verbose_name=_("Project name"), max_length=128)
    project_class = models.ForeignKey(
        "ProjectClass", verbose_name=_("Project Class"), on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name=_("Long description"),
        blank=True,
        null=False,
        help_text=_("Long description for the Project"),
    )

    def __str__(self):
        return self.name
