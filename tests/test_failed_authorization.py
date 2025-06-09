import requests
import pytest
from src.scenarios.scenario import ItemScenarios
from src.api.api_client import ItemApiClient


class TestFailedAuthorization:
    def test_create_item_without_token(self, item_data, unauthorized_scenario):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            unauthorized_scenario.only_create_item(item_data)

        assert exc_info.value.response.status_code == 401
        assert exc_info.value.response.json()["detail"] == "Not authenticated"
        print("✅ Запрет на создание item без токена работает. Получен status code 401 Unauthorized.")


    def test_get_items_without_token(self, unauthorized_scenario):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            unauthorized_scenario.get_and_verify_items_exist()

        assert exc_info.value.response.status_code == 401
        assert exc_info.value.response.json()["detail"] == "Not authenticated"
        print("✅ Запрет на получение items без токена работает. Получен status code 401 Unauthorized.")


    def test_edit_items_without_token(self, item_data, edited_item_data, unauthorized_scenario):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            unauthorized_scenario.update_item_and_verify_changes(item_data, edited_item_data)

        assert exc_info.value.response.status_code == 401
        assert exc_info.value.response.json()["detail"] == "Not authenticated"
        print("✅ Запрет на редактирование item без токена работает. Получен status code 401 Unauthorized.")
