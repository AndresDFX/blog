# Standard Library
from enum import Enum


class Group(str, Enum):
    ADMINS = "admins"
    BLOGGERS = "bloggers"
    EDITORS = "editors"
