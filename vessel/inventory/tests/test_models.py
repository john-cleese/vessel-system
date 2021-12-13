import pytest

from vessel.inventory.models import Inventory

pytestmark = pytest.mark.django_db


# Parada
class TestInventoryModel:
    def test_str(self, inventory: Inventory) -> None:
        assert inventory.name == str(inventory)

    def test_obj(self, inventory: Inventory) -> None:
        assert isinstance(inventory, Inventory)
