# Standard Library
from enum import Enum
from os import getenv
from typing import Any, Dict


class TokenTypes(Enum):
    ACCESS = "ACCESS"
    REFRESH = "REFRESH"


TOKEN_ALGORITHM = getenv("TOKEN_ALGORITHM", "HS256")

TOKEN_PROJECT_TYPES: Dict[str, Any] = {
    TokenTypes.ACCESS.value: {
        "expiration": getenv("TOKEN_EXPIRATION_ACCESS", 12)
    }
}
