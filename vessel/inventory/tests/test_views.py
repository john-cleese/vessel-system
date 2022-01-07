import json

import pytest
from model_bakery import baker

from vessel.django_assertions import assert_contains
from vessel.inventory.models import Item

pytestmark = [pytest.mark.django_db, pytest.mark.inventory]


class TestInventoryEndpoints:
    endpoint = "/api/inventory/"

    def test_list(self, api_client):
        baker.make(
            "inventory.Item", _quantity=3, _fill_optional=True, is_removed=False
        )

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        item = baker.prepare(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        expected_json = {"name": item.name, "qtd": item.qtd}

        response = api_client.post(self.endpoint, data=expected_json, format="json")

        assert_contains(response, "pk", status_code=201)
        assert_contains(response, expected_json["name"], status_code=201)
        assert_contains(response, expected_json["qtd"], status_code=201)

    def test_retrieve(self, api_client):
        item = baker.make(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        expected_json = {
            "pk": item.pk,
            "name": item.name,
            "qtd": item.qtd,
        }

        url = f"{self.endpoint}{item.pk}/"

        response = api_client.get(url)

        assert_contains(response, expected_json["pk"])
        assert_contains(response, expected_json["name"])
        assert_contains(response, expected_json["qtd"])

    def test_update(self, rf, api_client):
        old_item = baker.make(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        new_item = baker.prepare(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        item_dict = {"name": new_item.name, "qtd": new_item.qtd}

        url = f"{self.endpoint}{old_item.pk}/"

        response = api_client.put(url, item_dict, format="json")

        assert response.status_code == 200
        assert_contains(response, item_dict["name"])
        assert_contains(response, item_dict["qtd"])

    @pytest.mark.parametrize(
        "field",
        [
            ("name"),
            ("qtd"),
        ],
    )
    def test_partial_update(self, field, api_client):
        item = baker.make(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        item_dict = {
            "pk": item.pk,
            "name": item.name,
            "qtd": item.qtd,
        }

        valid_field = item_dict[field]
        url = f"{self.endpoint}{item.pk}/"

        response = api_client.patch(url, {field: valid_field}, format="json")

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client):
        item = baker.make(
            "inventory.Item", _fill_optional=True, is_removed=False
        )
        url = f"{self.endpoint}{item.pk}/"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert Item.objects.all().count() == 0
