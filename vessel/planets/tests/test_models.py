import pytest

from vessel.planets.models import Planet

pytestmark = pytest.mark.django_db


class TestPlanetModel:
    def test_str(self, planet: Planet) -> None:
        assert planet.name == str(planet)

    def test_obj(self, planet: Planet) -> None:
        assert isinstance(planet, Planet)
