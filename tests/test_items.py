import pytest
from config.constants import BASE_URL


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    @pytest.mark.order(1)
    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201),\
            f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]
        assert data.get("description") == item_data["description"]


        self.created_item_id = item_id


    @pytest.mark.order(2)
    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200,\
            f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"


    @pytest.mark.order(3)
    def test_put_items(self, item_data, auth_session):
        create_response = auth_session.post(f"{self.endpoint}", json=item_data)
        assert create_response.status_code in (200, 201),\
            f"Response: {create_response.status_code}, {create_response.text}"
        item_id = create_response.json()["id"]
        old_title = create_response.json()["title"]
        old_description = create_response.json()["description"]

        updated_data = {"title": "test_data", "description": "test"}
        response = auth_session.put(f"{self.endpoint}{item_id}", json=updated_data)
        assert response.status_code in (200, 201),\
            f"Response: {response.status_code}, {response.text}"

        new_data = response.json()
        assert new_data.get("id") == item_id, "IDs don't match"
        assert new_data.get("title") != old_title, "Titles match"
        assert new_data.get("title") != old_description, "Description match"


    @pytest.mark.order(4)
    def test_delete_items(self, item_data, auth_session):
        create_response = auth_session.post(f"{self.endpoint}", json=item_data)
        assert create_response.status_code in (200, 201), \
            f"Response: {create_response.status_code}, {create_response.text}"
        item_id = create_response.json()["id"]

        response = auth_session.delete(f"{self.endpoint}{item_id}")
        assert response.status_code in (200, 201), \
            f"Response: {response.status_code}, {response.text}"

        new_data = response.json()
        assert new_data.get("message") == "Item deleted successfully", "Item didn't delete"
        response = auth_session.get(f"{self.endpoint}{item_id}")
        assert response.status_code == 404, \
            f"Response: {response.status_code}, {response.text}"





