import pytest
from django.urls import resolve, reverse

from vessel.planets.models import Planet

pytestmark = pytest.mark.django_db


class TestPlanetUrls:
    def test_list(self) -> None:
        assert reverse("api:planet-list") == "/api/planets/"