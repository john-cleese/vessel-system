from django.db import models
from django.utils import timezone
from model_utils.models import UUIDModel

from vessel.core.managers import SoftDeletionManager


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class ModelBase(SoftDeletionModel, UUIDModel):
    class Meta:
        abstract = True
