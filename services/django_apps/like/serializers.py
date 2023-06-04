# Django
from django.contrib.auth.models import User
from rest_framework import serializers

from services.django_apps.comment.models import Comment
from services.django_apps.like.models import Like
from services.django_apps.post.models import Post


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False, allow_null=True
    )
    comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False, allow_null=True
    )

    def validate(self, attrs):
        post = attrs.get("post")
        comment = attrs.get("comment")

        if post is None and comment is None:
            raise serializers.ValidationError(
                "Debe proporcionar un valor para 'post' o 'comment'."
            )

        if post and comment:
            raise serializers.ValidationError(
                "Solo puede proporcionar un valor para 'post' o 'comment', no ambos."
            )

        return attrs

    class Meta:
        model = Like
        fields = "__all__"
