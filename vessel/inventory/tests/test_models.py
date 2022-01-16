import pytest

from vessel.inventory.models import Item

pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


# Parada
class TestItemModel:
    def test_str(self, item) -> None:
        assert item.name == str(item)

    def test_obj(self, item) -> None:
        assert isinstance(item, Item)

    def test_soft_delete(self, item) -> None:
        item.delete()
        assert Item.objects.count() == 0
        assert Item.all_objects.count() == 1

    def test_hard_delete(self, item) -> None:
        item.hard_delete()
        assert Item.objects.count() == 0
        assert Item.all_objects.count() == 0
