from faker import Faker
import pytest
import requests

from config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA, API_HEADERS


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/api/v1/login/access-token",
        data=AUTH_DATA, headers=AUTH_HEADERS
    )

    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token, "No access_token found"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


fake = Faker()

@pytest.fixture()
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }


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
def sql_injection():
    return {
        "title": "Valid_sql'; DROP TABLE users;--",
        "description": "Hack attempt"
    }


@pytest.fixture()
def xss_attack():
    return {
        "title": "Valid_xss",
        "description": "<script>alert('XSS');</script>"
    }


@pytest.fixture()
def data_with_extra_field():
    return {
        "title": "test123",
        "description": "test123",
        "extra_field": "123"
    }
