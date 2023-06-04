# Standard Library
import ipaddress

# Current Folder
from . import *  # noqa NOSONAR

ALLOWED_HOSTS = []
CORS_ORIGIN_WHITELIST = []


if environ.get("ALLOW_HOST") is not None:
    for host in environ.get("ALLOW_HOST", "").split(", "):
        ALLOWED_HOSTS += [
            "%s" % ip for ip in ipaddress.ip_network(host).hosts()
        ]

if environ.get("ALLOW_NAMES") is not None:
    ALLOWED_HOSTS += [
        "{0}".format(host_name.strip())
        for host_name in environ.get("ALLOW_NAMES", "").split(",")
    ]
    CORS_ORIGIN_WHITELIST += [
        "{0}".format(host_name.strip())
        for host_name in environ.get("ALLOW_ORIGIN_NAMES", "").split(",")
    ]


DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("DATABASE_NAME", "mydatabase"),
        "USER": environ.get("DATABASE_USER", "mydatabaseuser"),
        "PASSWORD": environ.get("DATABASE_PASSWORD", "mypassword"),
        "HOST": environ.get("DATABASE_HOST", "127.0.0.1"),
        "PORT": environ.get("DATABASE_PORT", "5432"),
    }
}


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS  # noqa
