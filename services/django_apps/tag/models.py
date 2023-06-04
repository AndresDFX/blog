# Django
from django.db import models

# Internal
from services.django_apps.utils.models.base import BaseModelUUID


class Tag(BaseModelUUID):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "tag"

    def __str__(self) -> str:
        return str(self.name)
