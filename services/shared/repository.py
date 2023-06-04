# Standard Library
import abc
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_M = TypeVar("_M")  # Generic models type


class AbstractReadRepository(Generic[_M]):
    @abc.abstractmethod
    def get(self, *args, **kwargs) -> _M:
        """Get an object"""


class AbstractWriteRepository(Generic[_M], ABC):
    @abstractmethod
    def add(self, *args, **kwargs) -> _M:
        """Add an object"""

    @abstractmethod
    def update(self, *args, **kwargs) -> _M:
        """Update an object"""


class AbstractRepository(
    AbstractReadRepository[_M], AbstractWriteRepository[_M]
):
    """Base class for repository patterns"""

    pass
