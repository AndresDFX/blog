# Standard Library
import datetime
import logging
from typing import Any, Dict, Optional, Union

# Libraries
import jwt
# Django
from rest_framework.exceptions import ValidationError

# Internal
from django_project.settings import SECRET_KEY
from services.shared.authentication.base_classes import TokenHandler
from services.shared.authentication.constants import (TOKEN_ALGORITHM,
                                                      TOKEN_PROJECT_TYPES)
from services.shared.tools import get_datetime_now

logger = logging.getLogger(__name__)


class JWTToken(TokenHandler):
    @classmethod
    def encode(
        cls,
        payload: Dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[Any] = None,
        type_: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ):
        alg = algorithm or TOKEN_ALGORITHM
        typ = type_ or "access"

        if type_.upper() not in TOKEN_PROJECT_TYPES.keys():
            raise ValueError(f"type {type_} not configured")
        expires = expires or get_datetime_now() + datetime.timedelta(
            hours=int(TOKEN_PROJECT_TYPES[typ.upper()].get("expiration"))
        )
        payload.update(exp=expires)
        headers = {"alg": alg, "typ": typ}
        token = jwt.encode(payload, key=SECRET_KEY, headers=headers)
        return token

    @classmethod
    def decode(cls, token: str, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        try:
            headers = jwt.get_unverified_header(token)
            payload = jwt.decode(
                token,
                key=SECRET_KEY,
                algorithms=[headers.get("alg")],
                options={"verify_signature": False},
            )
            expiration = payload.get("exp")
            now = datetime.datetime.now()
            expiration_date = cls.format_date(expiration)
            if now > expiration_date:
                logger.error("JWTToken :: decode :: Expired token")
                raise ValidationError("Expired token")
            payload |= headers
        except (
            jwt.DecodeError,
            jwt.ExpiredSignatureError,
            jwt.InvalidSignatureError,
        ) as error:
            logger.error(f"JWTToken :: decode :: {error}")
            raise ValidationError("Invalid token")

        return payload

    @classmethod
    def format_date(cls, expiration: Union[int, str]) -> datetime:
        if isinstance(expiration, int):  # unix timestamp to date object
            format_date = datetime.datetime.fromtimestamp(expiration)
        return format_date
