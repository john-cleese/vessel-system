import pytest

from vessel.planets.models import Planet

pytestmark = pytest.mark.django_db


class TestPlanetModel:
    def test_str(self, planet: Planet) -> None:
        assert planet.name == str(planet)

    def test_obj(self, planet: Planet) -> None:
        assert isinstance(planet, Planet)

    def test_soft_delete(self, planet: Planet) -> None:
        planet.delete()
        assert Planet.objects.count() == 0
        assert Planet.all_objects.count() == 1

    def test_hard_delete(self, planet: Planet) -> None:
        planet.hard_delete()
        assert Planet.objects.count() == 0
        assert Planet.all_objects.count() == 0
