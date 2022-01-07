# import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from vessel.inventory.api.serializers import ItemSerializer
from vessel.inventory.models import Item


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 200


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all().order_by("name")
    serializer_class = ItemSerializer
