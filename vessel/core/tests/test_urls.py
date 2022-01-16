import pytest
from django.urls import resolve, reverse

pytestmark = [pytest.mark.django_db, pytest.mark.core]


class TestSwaggerUrls:
    def test_schema(self, item) -> None:
        assert reverse("schema") == "/api/schema/"
        assert resolve("/api/schema/").view_name == "schema"

    def test_api_docs(self) -> None:
        assert reverse("swagger-ui") == "/api/docs/"
        assert resolve("/api/docs/").view_name == "swagger-ui"


class TestJWTUrls:
    def test_obtain_pair_token(self, item) -> None:
        assert reverse("token_obtain_pair") == "/api/token/"
        assert resolve("/api/token/").view_name == "token_obtain_pair"

    def test_refresh_token(self) -> None:
        assert reverse("token_refresh") == "/api/token/refresh/"
        assert resolve("/api/token/refresh/").view_name == "token_refresh"

    def test_obtain_auth_token(self) -> None:
        assert reverse("obtain_auth_token") == "/api/auth-token/"
        assert resolve("/api/auth-token/").view_name == "obtain_auth_token"
