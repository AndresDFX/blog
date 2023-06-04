# Standard Library
from datetime import timedelta
from typing import Dict

# Django
from django.contrib.auth.models import User

# Internal
from services.django_apps.authentication.adapters.repository import \
    DjangoUserRepository
from services.shared.authentication.constants import TOKEN_PROJECT_TYPES
from services.shared.authentication.jwt_handler import JWTToken
from services.shared.tools import get_datetime_now

repository = DjangoUserRepository()
token_handler = JWTToken()


def create_tokens(username: str) -> Dict[str, str]:
    payload = {}
    for type_, conf in TOKEN_PROJECT_TYPES.items():
        expires = get_datetime_now() + timedelta(
            hours=int(conf.get("expiration"))
        )
        payload[f"{type_.lower()}_token"] = token_handler.encode(
            payload={
                "username": username,
            },
            expires=expires,
            type_=type_,
        )
    return payload


def login(
    username: str,
) -> Dict[str, str]:
    user = repository.get(username)
    tokens = create_tokens(user.username)

    return tokens


def create_user(
    username: str,
    email: str,
    first_name: str,
    last_name: str,
    group: str,
) -> User:
    user = repository.add(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        group=group,
    )

    return user
