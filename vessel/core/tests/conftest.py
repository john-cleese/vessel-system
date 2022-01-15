import pytest
from model_bakery import baker

from vessel.inventory.models import Item


@pytest.fixture
def item(db, user) -> Item:
    item = baker.make("inventory.Item", _fill_optional=True, deleted_at=None)
    return item


"""
def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker('inventory')
"""
