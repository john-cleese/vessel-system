import json

import pytest
from model_bakery import baker

from vessel.django_assertions import assert_contains
from vessel.inventory.models import Inventory

pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


class TestInventoryEndpoints:
    endpoint = "/api/inventory/"

    def test_list(self, api_client):
        baker.make(
            "inventory.Inventory", _quantity=3, _fill_optional=True, is_removed=False
        )

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        inventory = baker.prepare(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        expected_json = {"name": inventory.name, "qtd": inventory.qtd}

        response = api_client.post(self.endpoint, data=expected_json, format="json")

        assert_contains(response, "pk", status_code=201)
        assert_contains(response, expected_json["name"], status_code=201)
        assert_contains(response, expected_json["qtd"], status_code=201)

    def test_retrieve(self, api_client):
        inventory = baker.make(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        expected_json = {
            "pk": inventory.pk,
            "name": inventory.name,
            "qtd": inventory.qtd,
        }

        url = f"{self.endpoint}{inventory.pk}/"

        response = api_client.get(url)

        assert_contains(response, expected_json["pk"])
        assert_contains(response, expected_json["name"])
        assert_contains(response, expected_json["qtd"])

    def test_update(self, rf, api_client):
        old_inventory = baker.make(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        new_inventory = baker.prepare(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        inventory_dict = {"name": new_inventory.name, "qtd": new_inventory.qtd}

        url = f"{self.endpoint}{old_inventory.pk}/"

        response = api_client.put(url, inventory_dict, format="json")

        assert response.status_code == 200
        assert_contains(response, inventory_dict["name"])
        assert_contains(response, inventory_dict["qtd"])

    @pytest.mark.parametrize(
        "field",
        [
            ("name"),
            ("qtd"),
        ],
    )
    def test_partial_update(self, field, api_client):
        inventory = baker.make(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        inventory_dict = {
            "pk": inventory.pk,
            "name": inventory.name,
            "qtd": inventory.qtd,
        }

        valid_field = inventory_dict[field]
        url = f"{self.endpoint}{inventory.pk}/"

        response = api_client.patch(url, {field: valid_field}, format="json")

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client):
        inventory = baker.make(
            "inventory.Inventory", _fill_optional=True, is_removed=False
        )
        url = f"{self.endpoint}{inventory.pk}/"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert Inventory.objects.all().count() == 0
