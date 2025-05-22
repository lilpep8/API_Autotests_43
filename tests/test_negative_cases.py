from config.constants import BASE_URL


class TestNegativeCases:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_invalid_data(self, invalid_data, auth_session):
        response = auth_session.post(self.endpoint, json=invalid_data)
        assert response.status_code == 422, \
            f"Response: {response.status_code}, {response.text}"

        error_message = response.json()
        assert "detail" in error_message, "Missing 'detail' in error response"

    # Отправка несуществующего поля
    def test_extra_field(self, data_with_extra_field, auth_session):
        response = auth_session.post(self.endpoint, json=data_with_extra_field)
        assert response.status_code in (200, 201), \
            f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("title") == data_with_extra_field["title"]
        assert data.get("description") == data_with_extra_field["description"]
        assert "extra_field" not in data

        item_id = data.get("id")
        delete_item = auth_session.delete(f"{self.endpoint}{item_id}")
        assert delete_item.status_code in (200, 201), \
            f"Error deleting element with id {item_id}"

        # Cleanup
        get_deleted_item= auth_session.get(f"{self.endpoint}{item_id}")
        assert get_deleted_item.status_code == 404, "Item was not deleted"

    # Обновление несуществующего элемента
    def test_put_a_non_existent_item(self, item_data, auth_session):
        item_id = "00000000-0000-0000-0000-000000000000"
        response = auth_session.put(f"{self.endpoint}{item_id}", json=item_data)
        assert response.status_code == 404, \
            f"Response: {response.status_code}, {response.text}"

        error_message = response.json()
        assert "detail" in error_message, "Missing 'detail' in error response"
        assert error_message["detail"] == "Item not found"

    # Удаление несуществующего элемента
    def test_delete_a_non_existent_item(self, item_data, auth_session):
        item_id = "00000000-0000-0000-0000-000000000000"
        deleted_item = auth_session.delete(f"{self.endpoint}{item_id}", json=item_data)
        assert deleted_item.status_code == 404, \
            f"Response: {deleted_item.status_code}, {deleted_item.text}"

        error_message = deleted_item.json()
        assert "detail" in error_message, "Missing 'detail' in error response"
        assert error_message["detail"] == "Item not found"


    # Удаление элемента **дважды**
    def test_deleting_item_twice(self, item_data, auth_session):
        created_response = auth_session.post(self.endpoint, json=item_data)
        assert created_response.status_code == 200, \
            f"Response: {created_response.status_code}, {created_response.text}"

        item_id = created_response.json()["id"]
        first_delete = auth_session.delete(f"{self.endpoint}{item_id}")
        assert first_delete.status_code in (200, 201), \
            f"Response: {first_delete.status_code}, {first_delete.text}"

        second_delete = auth_session.delete(f"{self.endpoint}{item_id}")
        assert second_delete.status_code == 404, \
            f"Response: {second_delete.status_code}, {second_delete.text}"

        error_message = second_delete.json()
        assert "detail" in error_message, "Missing 'detail' in error response"
        assert error_message["detail"] == "Item not found"


