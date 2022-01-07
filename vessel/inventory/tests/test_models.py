import pytest

from vessel.inventory.models import Item

pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


# Parada
class TestItemModel:
    def test_str(self, item) -> None:
        assert item.name == str(item)

    def test_obj(self, item) -> None:
        assert isinstance(item, Item)
