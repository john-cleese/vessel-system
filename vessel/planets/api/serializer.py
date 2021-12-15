from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from vessel.planets.models import Planet


class PlanetSerializer(ModelSerializer):
    class Meta:
        model = Planet
        fields = (
            "pk",
            "name",
            "total_area",
            "population",
            "discovery_date",
        )
