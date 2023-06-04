# Django
from rest_framework import permissions

from services.django_apps.post.serializers import PostSerializer
# Internal
from services.django_apps.utils.views.mixins import APIErrorsMixin
from services.django_apps.utils.views.permissions import IsEditor, IsOwner
from services.django_apps.utils.views.viewsets import GenericViewSet


class PostViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsOwner | permissions.IsAdminUser | IsEditor]
