# Standard Library
from typing import Any

# Django
from django.urls import include, path
from rest_framework import routers

# Internal
from services.django_apps.like import views

router = routers.DefaultRouter()
router.register("likes", views.LikeViewSet)

urlpatterns: list[Any] = [
    path("", include(router.urls)),
]
