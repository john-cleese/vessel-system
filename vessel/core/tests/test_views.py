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
    client = APIClient()

    def test_api_jwt(self, api_client):
        url = reverse('obtain_auth_token')
        user = get_user_model().objects.create_user(username='user', email='user@foo.com', password='pass')
        user.is_active = False
        user.save()

        resp = self.client.post(url, {'email': 'user@foo.com', 'password': 'pass'}, format='json')
        assert resp.status_code == status.HTTP_400_BAD_REQUEST

        user.is_active = True
        user.save()

        resp = self.client.post(url, {'username': 'user', 'password': 'pass'}, format='json')
        assert_contains(resp, 'token', status_code=200)

        token = resp.data['token']
        verification_url = reverse('token_verify')
        resp = self.client.post(verification_url, {'token': f'Bearer  {token}'}, format='json')
        print(f'asdf {token}')
        assert resp.status_code == status.HTTP_200_OK

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        client = APIClient()
        url = reverse('api:item-list')
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        resp = client.get(url, data={'format': 'json'})
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = client.get(url, data={'format': 'json'})
        assert resp.status_code == status.HTTP_200_OK
"""
