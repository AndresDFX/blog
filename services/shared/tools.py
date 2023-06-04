# Standard Library
from datetime import datetime
from enum import Enum
from typing import Any

# Django
from django.utils import timezone


def get_datetime_now() -> datetime:
    return timezone.localtime(timezone.now())


def enum_to_choices(obj: type[Enum]) -> list[tuple[Any, str]]:
    return [(elem.value.upper(), elem.name) for elem in iter(obj)]
