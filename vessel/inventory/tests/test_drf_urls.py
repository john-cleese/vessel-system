import pytest
from django.urls import resolve, reverse


pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


class TestItemUrls:
    def test_detail(self, item) -> None:
        assert (
            reverse("api:item-detail", args=(item.pk,))
            == f"/api/inventory/{item.pk}/"
        )
        assert (
            resolve(f"/api/inventory/{item.pk}/").view_name
            == "api:item-detail"
        )

    def test_list(self) -> None:
        assert reverse("api:item-list") == "/api/inventory/"
        assert resolve("/api/inventory/").view_name == "api:item-list"
