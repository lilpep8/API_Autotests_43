from src.config.api_constants import api_config


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL  # Можно также передавать в конструктор, если он может меняться

    def create_item(self, item_data):
        """Отправляет запрос на создание item."""
        response = self.auth_session.post(f"{self.base_url}/api/v1/items/", json=item_data.model_dump())
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response

    def get_items(self):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/api/v1/items/")
        if response.status_code != 200:
            response.raise_for_status()
        return response

    def update_item(self, item_id, upd_item_data):
        """Отправляет запрос на обновление item."""
        response = self.auth_session.put(f"{self.base_url}/api/v1/items/{item_id}", json=upd_item_data.model_dump())
        if response.status_code != 200:
            response.raise_for_status()
        return response

    def delete_item(self, item_id):
        """Отправляет запрос на удаление item."""
        response = self.auth_session.delete(f"{self.base_url}/api/v1/items/{item_id}")
        if response.status_code != 200: # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response # или response.status_code


    def get_item(self, item_id):
        """Отправляет запрос на получение item по id."""
        response = self.auth_session.get(f"{self.base_url}/api/v1/items/{item_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response


    def create_item_unchecked(self, invalid_item_data: dict):
        """
        Отправляет запрос на создание item с невалидными данными(без проверки кода ошибок).
        Требуется для негативных кейсов.
        """
        return self.auth_session.post(f"{self.base_url}/api/v1/items/", json=invalid_item_data)

