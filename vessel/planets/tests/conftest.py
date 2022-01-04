import pytest
from model_bakery import baker

from vessel.planets.models import Planet


@pytest.fixture
def planet(db) -> Planet:
    planet = baker.make("planets.Planet", _fill_optional=True, is_removed=False)
    return planet
