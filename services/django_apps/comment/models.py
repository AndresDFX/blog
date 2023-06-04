# Django
from django.contrib.auth.models import User
from django.db import models

# Internal
from services.django_apps.post.models import Post
from services.django_apps.utils.models.base import BaseModelUUID


class Comment(BaseModelUUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = "comment"
