from src.scenarios.negative_scenarios import ItemNegativeScenarios
from src.api.api_client import ItemApiClient


class TestNegativeCases:
    def test_invalid_data(self, invalid_data, auth_session):
        scenario = ItemNegativeScenarios(api_client=ItemApiClient(auth_session))
        response_about_error = scenario.create_invalid_data(invalid_data)
        assert response_about_error is not None


    def test_item_with_extra_field(self, data_with_extra_field, auth_session):
        scenario = ItemNegativeScenarios(api_client=ItemApiClient(auth_session))
        item_id = scenario.create_with_extra_field(data_with_extra_field)
        assert item_id is not None


    def test_deleting_item_twice(self, item_data, auth_session):
        scenario = ItemNegativeScenarios(api_client=ItemApiClient(auth_session))
        scenario.delete_item_twice(item_data)


    def test_edit_a_non_existent_item(self, auth_session, item_data, edited_item_data):
        scenario = ItemNegativeScenarios(api_client=ItemApiClient(auth_session))
        scenario.edit_a_non_existent_item(item_data, edited_item_data)
