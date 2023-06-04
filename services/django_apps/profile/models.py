# Django
from django.contrib.auth.models import User
from django.db import models

# Internal
from services.django_apps.utils.models.base import BaseModelUUID


class Profile(BaseModelUUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    profile_image = models.ImageField(upload_to="profile_images/")

    class Meta:
        db_table = "profile"
