# Standard Library
from typing import Any, Dict, Optional, Tuple, TypeVar

# Libraries
import jwt
# Django
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

# Internal
from services.django_apps.authentication.adapters.repository import \
    DjangoUserRepository
from services.domain.authentication.adapters.repository import \
    AbstractUserRepository
from services.shared.authentication.base_classes import Authenticator
from services.shared.authentication.jwt_handler import JWTToken

request_object = TypeVar("request_object", bound=Request)


class JWTAuthenticator(Authenticator):
    def __init__(self, repository: Optional[AbstractUserRepository] = None):
        self.repository = repository or DjangoUserRepository()

    def authenticate(
        self, request: request_object, **kwargs: Dict[str, Any]
    ) -> Optional[Tuple[User, str]]:
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise ValidationError("token not provided")
        try:
            payload = JWTToken.decode(token.split(" ")[1])
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError) as e:
            raise ValidationError(str(e))

        customer = self.authenticate_credentials(payload)
        return customer, token

    def authenticate_credentials(self, payload: Dict[str, Any]) -> User:
        username = payload.get("username")
        if not username:
            raise ValidationError("token malformed")
        user = self.repository.get(username=username)

        return user
