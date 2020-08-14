from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class IndexedTimeStampedModel(models.Model):
    created_at = AutoCreatedField(_("created"), db_index=True)
    updated_at = AutoLastModifiedField(_("modified"), db_index=True)

    class Meta:
        abstract = True
