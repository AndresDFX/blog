# Standard Library
from typing import Any

# Django
from django.urls import include, path
from rest_framework import routers

# Internal
from services.django_apps.authentication import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("profiles", views.ProfileViewSet)

urlpatterns: list[Any] = [
    path("", views.GenerateTokenView.as_view(), name="generate-token"),
    path("", include(router.urls)),
]
