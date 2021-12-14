import pytest
from model_bakery import baker

from vessel.inventory.models import Inventory


@pytest.fixture
def inventory(db, user) -> Inventory:
    inventory = baker.make("inventory.Inventory", _fill_optional=True, is_removed=False)
    return inventory