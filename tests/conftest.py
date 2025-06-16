from faker import Faker
import pytest
import requests
from src.data_models.models import ItemResponse
from src.api.api_client import ItemApiClient
from src.scenarios.scenario import ItemScenarios
from src.config.api_constants import api_config


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{api_config.BASE_URL}/api/v1/login/access-token",
        data=api_config.AUTH_DATA, headers=api_config.AUTH_HEADERS
    )

    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token, "No access_token found"

    session.headers.update(api_config.API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture
def unauthorized_scenario():
    no_auth_session = requests.Session()
    return ItemScenarios(api_client=ItemApiClient(no_auth_session))


fake = Faker()

@pytest.fixture()
def item_data():
    return ItemResponse(
        title=fake.word().capitalize(),
        description=fake.sentence(nb_words=10)
    )


@pytest.fixture()
def edited_item_data():
    return ItemResponse(
        title=fake.word().capitalize(),
        description=fake.sentence(nb_words=10)
    )


@pytest.fixture(params=[
    {"title": "", "description": fake.sentence(nb_words=10)},  # Пустой title
    {"title": None, "description": fake.sentence(nb_words=10)},  # None в title
    {"title": "x" * 1001, "description": fake.sentence(nb_words=10)},  # Слишком длинный title
    {"title": 123, "description": "valid"}, # Неправильный тип
    {"description": "valid"}, # Отсутствие обязательного поля title
    {} # Пустой json
    ])


def invalid_data(request):
    return request.param


@pytest.fixture()
def data_with_extra_field():
    return {
        "title": "test123",
        "description": "test123",
        "extra_field": "123"
    }
