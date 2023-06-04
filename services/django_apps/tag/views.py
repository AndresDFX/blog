# Django
from rest_framework import permissions

from services.django_apps.tag.serializers import TagSerializer
# Internal
from services.django_apps.utils.views.mixins import APIErrorsMixin
from services.django_apps.utils.views.viewsets import GenericViewSet


class TagViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
