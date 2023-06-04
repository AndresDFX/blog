# Libraries
import django_filters
from django.db import models
from django_filters import filters


class GenericFilter(django_filters.FilterSet):
    @classmethod
    def filter_for_field(cls, f, name, lookup_expr="exact"):
        if isinstance(f, models.ImageField):
            return filters.CharFilter(field_name=name, lookup_expr=lookup_expr)
        return super().filter_for_field(f, name, lookup_expr)

    class Meta:
        model = None
        fields = "__all__"
