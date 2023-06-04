# Django
from django.contrib.auth.models import User
from rest_framework import serializers

from services.django_apps.post.models import Post
from services.django_apps.tag.models import Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    tags = serializers.SlugRelatedField(
        slug_field="name", queryset=Tag.objects.all(), many=True
    )

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags_data)
        return post
