# Django
from django.contrib.auth.models import User
from django.db import models

# Internal
from services.django_apps.tag.models import Tag
from services.django_apps.utils.models.base import BaseModelUUID


class Post(BaseModelUUID):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = "post"
