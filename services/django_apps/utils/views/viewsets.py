from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from services.django_apps.utils.views.filters import GenericFilter
from services.django_apps.utils.views.pagination import GlobalPagination
from services.shared.authentication.authenticators import JWTAuthenticator


class GenericViewSet(ModelViewSet):
    serializer_class = None
    queryset = User.objects.all()  # any model
    filterset_class = GenericFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    pagination_class = GlobalPagination
    authentication_classes = (JWTAuthenticator,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model = self.serializer_class.Meta.model
        filter_fields = [field.name for field in model._meta.fields]
        self.filterset_class = type(
            "DynamicFilterSet",
            (GenericFilter,),
            {
                "Meta": type(
                    "Meta", (), {"model": model, "fields": filter_fields}
                )
            },
        )
        self.queryset = self.get_queryset()

    def get_queryset(self):
        serializer_class = self.get_serializer_class()
        model = serializer_class.Meta.model
        return model.objects.all()
