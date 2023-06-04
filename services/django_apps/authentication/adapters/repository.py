# Standard Library
import logging
from typing import Dict, List, Optional

# Django
from django.contrib.auth.models import Group, User
from django.core import exceptions as django_exceptions
from django.core.exceptions import ValidationError


# Internal
from services.domain.authentication import constants
from services.domain.authentication.adapters.repository import \
    AbstractUserRepository
from services.shared.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


class DjangoUserRepository(AbstractUserRepository):
    def get(self, username: str) -> Optional[User]:
        try:
            user = User.objects.get(username=username)
            return user
        except django_exceptions.ObjectDoesNotExist as e:
            logger.error(f"DjangoUserRepository :: get :: error {e}")
            raise ObjectDoesNotExist("user does not exists")

    def add(
        self,
        username: str,
        email: str,
        first_name: str,
        last_name: str,
        groups: List[str],
        password: str = "",
    ) -> Optional[User]:
        try:
            is_staff = any(
                group == constants.Group.ADMINS.value for group in groups
            )
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_staff=is_staff,
                password=password,
            )
            user.groups.set(Group.objects.filter(name__in=groups))
            return user
        except Exception as e:
            logger.error(f"DjangoUserRepository :: add :: error {e}")
            raise ValidationError("error to create user")

    def update(
        self,
        user_id: str,
        values: Dict,
    ) -> Optional[User]:
        try:
            groups = values.get("groups")
            if groups:
                is_staff = any(
                    g == constants.Group.ADMINS.value for g in groups
                )
                values["is_staff"] = is_staff
                values.pop("groups")

            user, created = User.objects.update_or_create(
                id=user_id,
                defaults=values,
            )

            if groups:
                user.groups.set(Group.objects.filter(name__in=groups))

            return user
        except Exception as e:
            logger.error(f"DjangoUserRepository :: update :: error {e}")
            raise ValidationError("error to update user")
