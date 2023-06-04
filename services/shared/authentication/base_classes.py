# Standard Library
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Optional, Tuple, TypeVar

# Django
from django.contrib.auth.models import User

# Internal
from services.domain.authentication.adapters.repository import \
    AbstractUserRepository

Token = TypeVar("Token", bound=str)


class TokenHandler(ABC):
    @abstractmethod
    def encode(
        self,
        payload: Dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[datetime] = None,
        type_: Optional[str] = None,
        **kwargs: Dict[str, Any]
    ) -> Token:
        """Create a signed token based on specific parameters"""

    @abstractmethod
    def decode(self, token: str, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Extract info from a signed object or token"""


class Authenticator(ABC):
    repository: AbstractUserRepository

    @abstractmethod
    def authenticate(
        self, request: Any, **kwargs: Dict[str, Any]
    ) -> Optional[Tuple[User, Token]]:
        """Authenticate and extract user if it is applicable"""


class Permission(ABC):
    @abstractmethod
    def has_permission(self, request: Any) -> bool:
        """Validates is validators has a permission to continue"""
