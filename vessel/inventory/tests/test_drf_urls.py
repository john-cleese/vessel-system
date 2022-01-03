import pytest
from django.urls import resolve, reverse

from vessel.inventory.models import Inventory

pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


class TestInventoryUrls:
    def test_detail(self, inventory: Inventory) -> None:
        assert (
            reverse("api:inventory-detail", args=(inventory.pk,))
            == f"/api/inventory/{inventory.pk}/"
        )
        assert (
            resolve(f"/api/inventory/{inventory.pk}/").view_name
            == "api:inventory-detail"
        )

    def test_list(self) -> None:
        assert reverse("api:inventory-list") == "/api/inventory/"
        assert resolve("/api/inventory/").view_name == "api:inventory-list"
