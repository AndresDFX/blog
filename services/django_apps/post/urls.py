# Standard Library
from typing import Any

# Django
from django.urls import include, path
from rest_framework import routers

# Internal
from services.django_apps.post import views

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns: list[Any] = [
    path("", include(router.urls)),
]
