# Django
from django.contrib.auth.models import User
from django.db import models

# Internal
from services.django_apps.comment.models import Comment
from services.django_apps.post.models import Post
from services.django_apps.utils.models.base import BaseModelUUID


class Like(BaseModelUUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "like"
        constraints = [
            models.CheckConstraint(
                check=models.Q(post_id__isnull=False)
                | models.Q(comment_id__isnull=False),
                name="post_or_comment",
            )
        ]
