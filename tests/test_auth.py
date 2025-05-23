from config.constants import BASE_URL
import requests
import pytest


class TestFailedAuthorization:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_post_item_without_token(self, item_data):
        no_auth_session = requests.Session()  # Чистая сессия без токена
        response = no_auth_session.post(self.endpoint, json=item_data)

        assert response.status_code == 401, \
            f"Response: {response.status_code}, {response.text}"
        assert response.json()["detail"] == "Not authenticated"


    def test_get_items_without_token(self):
        no_auth_session = requests.Session()
        response = no_auth_session.get(self.endpoint)

        assert response.status_code == 401,\
            f"Response: {response.status_code}, {response.text}"
        assert response.json()["detail"] == "Not authenticated"


    def test_delete_items_without_token(self, item_data, auth_session):
        created_response_with_token = auth_session.post(f"{self.endpoint}", json=item_data)
        assert created_response_with_token.status_code in (200, 201), \
            f"Response: {created_response_with_token.status_code}, {created_response_with_token.text}"
        item_id = created_response_with_token.json()["id"]
        auth_session.close()

        no_auth_session = requests.Session()
        response = no_auth_session.delete(f"{self.endpoint}{item_id}")

        assert response.status_code == 401,\
            f"Response: {response.status_code}, {response.text}"
        assert response.json()["detail"] == "Not authenticated"
