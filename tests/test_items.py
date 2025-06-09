import pytest

from src.scenarios.scenario import ItemScenarios
from src.api.api_client import ItemApiClient


class TestCrudItems:

    def test_create_item(self, item_data, auth_session):
        scenario = ItemScenarios(api_client=ItemApiClient(auth_session))
        item_id = scenario.create_item_and_immediately_delete(item_data)
        assert item_id is not None


    def test_get_items(self, auth_session):
        scenario = ItemScenarios(api_client=ItemApiClient(auth_session))
        items = scenario.get_and_verify_items_exist()
        assert items is not None


    def test_edit_item(self, auth_session, item_data, edited_item_data):
        scenario = ItemScenarios(api_client=ItemApiClient(auth_session))
        item_id = scenario.update_item_and_verify_changes(item_data, edited_item_data)
        assert item_id is not None
        scenario.delete_existing_item_and_verify(item_id)


    def test_delete_item(self, auth_session, item_data):
        scenario = ItemScenarios(api_client=ItemApiClient(auth_session))
        item_id = scenario.only_create_item(item_data)
        assert item_id is not None
        scenario.delete_existing_item_and_verify(item_id)
