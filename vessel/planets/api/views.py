from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from vessel.planets.api.serializer import PlanetSerializer
from vessel.planets.models import Planet


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all().order_by("name")
    serializer_class = PlanetSerializer
