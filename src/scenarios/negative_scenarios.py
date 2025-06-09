from src.api.api_client import ItemApiClient
import requests


class ItemNegativeScenarios:
    def __init__(self, api_client: ItemApiClient):  # Типизация для ясности
        self.api_client = api_client


    def create_invalid_data(self, invalid_item_data):
        """
        Сценарий: отправляет невалидные данные item и проверяет код ошибок и сообщения.
        """
        response = self.api_client.create_item_unchecked(invalid_item_data)
        assert response.status_code == 422, \
            f"Response: {response.status_code}, {response.text}"
        assert response.status_code != 500,\
            f"Auth failed: {response.status_code}, {response.text}"

        error_message = response.json()
        assert "detail" in error_message, "Missing 'detail' in error response"
        print(f"Запросы с невалидными данными были отклонены со статус кодом {response.status_code}")
        return error_message


    def create_with_extra_field(self, data_with_extra_field):
        """
        Сценарий: Отправка несуществующего item с несуществующим полем, проверка отсутствия этого поля.
        """
        response_created_item_data_with_extra_field = self.api_client.create_item_unchecked(data_with_extra_field)

        extra_item_id = response_created_item_data_with_extra_field.json().get("id")
        assert extra_item_id is not None, f"ID не найден в ответе на создание: {created_item_data_with_extra_field}"

        assert response_created_item_data_with_extra_field.json().get("title") == data_with_extra_field["title"]
        assert response_created_item_data_with_extra_field.json().get("description") == data_with_extra_field["description"]
        assert "extra_field" not in response_created_item_data_with_extra_field.json()

        self.api_client.delete_item(extra_item_id)
        print(f"Item с ID {extra_item_id} успешно создан без дополнительного поля и удален.")
        return extra_item_id


    def delete_item_twice(self, item_data):
        """
        Сценарий: Удаление элемента **дважды**.
        """
        created_response = self.api_client.create_item(item_data)
        item_id = created_response.json().get("id")
        self.api_client.delete_item(item_id)
        # Попытка второго удаления
        try:
            self.api_client.delete_item(item_id)
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404
            error_message = e.response.json()
            assert error_message.get("detail") == "Item not found"
        else:
            raise AssertionError("Ожидалась ошибка 404, но она не произошла")
        print("Удаление Item дважды не вызвало ошибок")



    def edit_a_non_existent_item(self, item_data, edited_item_data):
        """
        Сценарий: Обновление несуществующего элемента.
        """
        created_response = self.api_client.create_item(item_data)
        item_id = created_response.json().get("id")
        self.api_client.delete_item(item_id)
        # Попытка редактирования удаленного элемента
        try:
            self.api_client.update_item(item_id,edited_item_data)
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404
            error_message = e.response.json()
            assert error_message.get("detail") == "Item not found"
        else:
            raise AssertionError("Ожидалась ошибка 404, но она не произошла")
        print("Редактирование удаленного Item не вызвало ошибок")
