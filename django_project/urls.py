# Django
from django.conf import settings
from django.urls import URLPattern, include, path

public_urls: list[URLPattern] = [
    path("auth/", include("services.django_apps.authentication.urls")),
    path("", include("services.django_apps.comment.urls")),
    path("", include("services.django_apps.like.urls")),
    path("", include("services.django_apps.post.urls")),
    path("", include("services.django_apps.tag.urls")),
]

internal_urls: list[URLPattern] = []


urlpatterns = internal_urls if settings.IS_INTERNAL else public_urls

if settings.DEBUG is True:
    # Libraries
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
