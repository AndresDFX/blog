# Standard Library
from uuid import UUID

# Django
from django.urls import resolve
from rest_framework import permissions

# Internal
from services.domain.authentication.constants import Group


class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=Group.EDITORS.name).exists()


class IsOwnerProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == "DELETE" and not request.user.is_staff:
            return False
        elif request.method == "POST":
            user = request.POST["user"]
            return user == str(request.user.id)
        else:
            resolved_match = resolve(request.path)
            profile = resolved_match.kwargs.get("pk")
            return request.user.profile.id == UUID(profile)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            view.action == "create"
            or view.action == "retrieve"
            or view.action == "update"
            or view.action == "partial_update"
            or view.action == "destroy"
        ):
            return obj.author == request.user

        return False
