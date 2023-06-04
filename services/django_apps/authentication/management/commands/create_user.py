# Standard Library
import logging

# Django
from django.core.management import BaseCommand

# Internal
from services.domain.authentication.constants import Group
from services.domain.authentication.service_layer import handlers

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """
        Create an user

        Example of use:
        python manage.py create_user \
            --username=pepito@letsdoitnow.us  \
            --first_name=Pepito \
            --last_name=Perez \
            --email=pepito@letsdoitnow.us \
            --group=ADMINS \
    """

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True, nargs="?", type=str)
        parser.add_argument("--first_name", nargs="?", type=str)
        parser.add_argument("--last_name", nargs="?", type=str)
        parser.add_argument("--email", nargs="?", type=str)
        parser.add_argument(
            "--group",
            required=True,
            nargs="?",
            type=str,
            choices=[elem.name for elem in iter(Group)],
        )

    def handle(self, *args, **options):
        logger.info(f"create_user :: called with {options} options")

        user = handlers.create_user(
            username=options.pop("username"),
            email=options.pop("email"),
            group=options.pop("group"),
            first_name=options.pop("first_name", ""),
            last_name=options.pop("last_name", ""),
        )

        logger.info(f"create_user :: user {user.id} created.")
