import pytest
from django.urls import resolve, reverse

from vessel.inventory.models import Inventory

pytestmark = pytest.mark.django_db


class TestInventoryUrls:
    def test_detail(self, inventory: Inventory) -> None:
        assert (
            reverse("api:inventory-detail", args=(inventory.pk,))
            == f"/inventory/{inventory.pk}/"
        )
        assert (
            resolve(f"/inventory/{inventory.pk}/").view_name == "api:inventory-detail"
        )

    def test_update(self, inventory: Inventory) -> None:
        assert (
            reverse("api:inventory-update", args=(inventory.pk,))
            == f"/inventory/{inventory.pk}/update/"
        )
        assert (
            resolve(f"/inventory/{inventory.pk}/update/").view_name
            == "api:inventory-update"
        )

    def test_list(self) -> None:
        assert reverse("api:inventory-list") == "/inventory/"
        assert resolve("/inventory/").view_name == "api:inventory-list"

    def test_create(self) -> None:
        assert reverse("api:inventory-create") == "/inventory/create/"
        assert resolve("/inventory/create/").view_name == "api:inventory-create"

    def test_delete(self, inventory: Inventory) -> None:
        assert (
            reverse("api:inventory-delete", args=(inventory.pk,))
            == f"/inventory/{inventory.pk}/delete/"
        )
        assert (
            resolve(f"/inventory/{inventory.pk}/delete/").view_name
            == "api:inventory-delete"
        )
