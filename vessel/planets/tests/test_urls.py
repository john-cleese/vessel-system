import pytest
import json
from django.urls import reverse, resolve
from model_bakery import baker

from vessel.planets.models import Planet

pytestmark = pytest.mark.django_db


class TestPlanetUrls:
    def test_list(self) -> None:
        assert reverse("api:planet-list") == "/api/planets/"
        assert resolve("/api/planets/").view_name == "api:planet-list"

    # def test_create(self) -> None:
    #     assert reverse("api:planet-create") == "/planet/create/"
    #     assert resolve("/planet/create/").view_name == "api:planet-create"

    def test_detail(self, planet):
        assert (
            reverse("api:planet-detail", args=(planet.pk,)) == f"/api/planets/{planet.pk}/"
        )
        assert (
            resolve(f"/api/planets/{planet.pk}/").view_name == "api:planet-detail"
        )

    # def test_delete(self, planet: Planet) -> None:
    #     assert reverse("api:planet-delete", kwargs={"pk": planet.pk}) == f"/planet/delete/{planet.pk}"
    #     assert resolve(f"/planet/delete/{planet.pk}").view_name == "api:planet-delete"