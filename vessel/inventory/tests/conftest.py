import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from vessel.inventory.models import Inventory


from vessel.inventory.models import Inventory


@pytest.fixture
def inventory(db, user) -> Inventory:
    inventory = baker.make("inventory.Inventory", _fill_optional=True, is_removed=False)
    return inventory

'''
def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker('inventory')
'''
