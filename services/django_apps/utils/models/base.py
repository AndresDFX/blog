# Standard Library
import uuid

# Django
from django.db import models


class BaseModel(models.Model):
    """Base Model to be implemented in all models.

    Attributes:
        created_at: A Datetime to specify the time when the object was created
        updated_at: A Datetime to specify the time when the object was updated
    """

    CASE_STYLE = "lower"

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created at"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def clean(self):
        fields_to_clean = getattr(self, "FIELDS_TO_CLEAN", None)
        fields = self._meta.fields

        if not fields_to_clean:
            return

        for field in fields:
            name = field.name
            if name in fields_to_clean:
                value = getattr(self, name)

                if value is None:
                    continue

                cleaned_value = value.strip()
                if self.CASE_STYLE and hasattr(str, self.CASE_STYLE):
                    cleaned_value = getattr(cleaned_value, self.CASE_STYLE)()

                setattr(self, name, cleaned_value)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseModelUUID(BaseModel):
    """Base Model to be implemented in all models.

    The difference with the BaseModel is the ID or PK is an uuid.

    Any model that has FIELDS_TO_CLEAN declared those fields would be lowered
    and removed additional white spaces

    Attributes:
        identifier: A UUID4 value to identify an object.
        created_at: A Datetime to specify the time when the object was created
        updated_at: A Datetime to specify the time when the object was updated
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
