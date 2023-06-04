# Django
from django.contrib.auth.models import User

# Internal
from services.shared.repository import AbstractRepository


class AbstractUserRepository(AbstractRepository[User]):
    """Base class for User repository"""

    pass
