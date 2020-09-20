from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField

from . import JobStatus


class IndexedTimeStampedModel(models.Model):
    created_at = AutoCreatedField(_("created"), db_index=True)
    updated_at = AutoLastModifiedField(_("modified"), db_index=True)

    class Meta:
        abstract = True


class Job(models.Model):
    status = models.CharField(max_length=50, choices=JobStatus.CHOICES, default=JobStatus.PENDING)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = AutoCreatedField(_("created"), db_index=True)
    updated_at = AutoLastModifiedField(_("modified"), db_index=True)

    class Meta:
        abstract = True
