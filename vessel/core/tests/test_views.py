import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db, pytest.mark.core]


class TestSwaggerEndpoints:
    def test_schema(self, api_client):
        response = api_client.get(reverse("schema"))
        assert response.status_code == 200

    def test_swagger_ui(self, api_client):
        response = api_client.get(reverse("swagger-ui"))
        assert response.status_code == 200


"""
class TestJWTEndpoints:
    def test_schema(self, api_client):
        response = api_client.get(reverse("schema"))
        assert response.status_code == 200

    def test_swagger_ui(self, api_client):
        response = api_client.get(reverse("swagger-ui"))
        assert response.status_code == 200
"""
