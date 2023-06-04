# Django
from rest_framework import permissions

from services.django_apps.comment.serializers import CommentSerializer
# Internal
from services.django_apps.utils.views.mixins import APIErrorsMixin
from services.django_apps.utils.views.permissions import IsEditor, IsOwner
from services.django_apps.utils.views.viewsets import GenericViewSet


class CommentViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwner | permissions.IsAdminUser | IsEditor]
