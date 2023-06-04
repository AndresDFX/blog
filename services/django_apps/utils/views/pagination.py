# Standard Library
import os

# Django
from rest_framework.pagination import PageNumberPagination


class GlobalPagination(PageNumberPagination):
    page_size = int(os.getenv("DEFAULT_PAGINATE", "3"))
    page_size_query_param = "page_size"
    max_page_size = 100
