from src.api.api_client import ItemApiClient
from src.utils.response_validator import validate_response
from src.data_models.models import ItemResponse


class ItemScenarios:
    def __init__(self, api_client: ItemApiClient):  # Типизация для ясности
        self.api_client = api_client

    def create_item_and_immediately_delete(self, item_data):
        """
        Сценарий: создать item, валидировать и сразу же его удалить.
        Возвращает ID созданного и удаленного item.
        """
        created_item_data = self.api_client.create_item(item_data)
        item_id = created_item_data.json().get("id")
        assert item_id is not None, f"ID не найден в ответе на создание: {created_item_data}"
        
        validate_response(
            created_item_data,
            model=ItemResponse,
            expected_data=item_data.model_dump()
        )

        self.api_client.delete_item(item_id)  # Проверка на успешность удаления внутри delete_item (raise_for_status)
        # или можно проверить статус ответа здесь, если delete_item его возвращает
        print(f"✅ Item с ID {item_id} успешно создан и удален.")
        return item_id

    def get_and_verify_items_exist(self):
        """
        Сценарий: получить список items и проверить, что он не пуст.
        """
        items = self.api_client.get_items().json()
        assert len(items) > 0, "Список items пуст"
        print(f"✅ Получено {len(items)} items.")
        return items

    def update_item_and_verify_changes(self, item_data, upd_item_data):
        """
        Сценарий: создать, обновить item и проверить, что данные изменились.
        Возвращает ID отредактированного item.
        """
        created_item_data = self.api_client.create_item(item_data)

        validate_response(
            created_item_data,
            model=ItemResponse,
            expected_data=item_data.model_dump()
        )

        item_id = created_item_data.json().get("id")
        updated_item = self.api_client.update_item(item_id, upd_item_data)

        validate_response(
            updated_item,
            model=ItemResponse,
            expected_data=upd_item_data.model_dump()
        )

        updated_item_data = updated_item.json()
        assert updated_item_data["description"] == upd_item_data.description, \
            f"Описание не обновилось. Ожидалось: {upd_item_data['description']}, получено: {updated_item['description']}"
        assert updated_item_data["title"] == upd_item_data.title, \
            f"Заголовок не обновился. Ожидалось: {upd_item_data['title']}, получено: {updated_item['title']}"
        print(f"✅ Item с ID {item_id} успешно обновлен.")

        return item_id

    def delete_existing_item_and_verify(self, item_id):  # test_item переименован в item_id для ясности
        """
        Сценарий: удалить существующий item и убедиться, что он удален.
        """
        self.api_client.delete_item(item_id)
        print(f"✅ Item с ID {item_id} отправлен на удаление.")
    
    
    def only_create_item(self, item_data):
        """
        Сценарий: создать item.
        Возвращает ID созданного item.
        """
        created_item_data = self.api_client.create_item(item_data).json()
        item_id = created_item_data.get("id")
        assert item_id is not None, f"ID не найден в ответе на создание: {created_item_data}"

        print(f"✅ Item с ID {item_id} успешно создан.")
        return item_id