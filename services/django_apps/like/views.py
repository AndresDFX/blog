# Django
from rest_framework import permissions

from services.django_apps.like.serializers import LikeSerializer
# Internal
from services.django_apps.utils.views.mixins import APIErrorsMixin
from services.django_apps.utils.views.permissions import IsEditor, IsOwner
from services.django_apps.utils.views.viewsets import GenericViewSet


class LikeViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsOwner | permissions.IsAdminUser | IsEditor]
