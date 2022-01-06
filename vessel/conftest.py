import pytest
from rest_framework.test import APIClient

from vessel.users.models import User
from vessel.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def user() -> User:
    return UserFactory()
