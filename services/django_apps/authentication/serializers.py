# Django
from django.contrib.auth.models import Group, User
from rest_framework import serializers

# Internal
from services.django_apps.authentication.adapters.repository import \
    DjangoUserRepository
from services.django_apps.profile.models import Profile

repository = DjangoUserRepository()


class TokenInputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Group.objects.all(),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "groups",
        ]
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": False},
            "password": {"write_only": True, "required": False},
            "first_name": {"required": False},
            "last_name": {"required": False},
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "biography", "profile_image"]
