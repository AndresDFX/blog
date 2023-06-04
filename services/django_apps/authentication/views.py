# Django
from django.urls import resolve
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
from services.django_apps.authentication.adapters.repository import \
    DjangoUserRepository
from services.django_apps.authentication.serializers import (
    ProfileSerializer, TokenInputSerializer, UserSerializer)
from services.django_apps.utils.views.mixins import APIErrorsMixin
from services.django_apps.utils.views.permissions import IsOwnerProfile
from services.django_apps.utils.views.viewsets import GenericViewSet
from services.domain.authentication.service_layer import handlers

repository = DjangoUserRepository()


class GenerateTokenView(APIErrorsMixin, APIView):
    def post(self, request: Request):
        serialize = TokenInputSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        access_tokens = handlers.login(username=serialize.data.get("username"))
        return Response(access_tokens, status=status.HTTP_200_OK)


class UserViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        repository.add(**serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resolved_match = resolve(request.path)
        user_id = resolved_match.kwargs.get("pk")
        repository.update(user_id=user_id, values=serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_200_OK, headers=headers
        )


class ProfileViewSet(APIErrorsMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerProfile | permissions.IsAdminUser]
