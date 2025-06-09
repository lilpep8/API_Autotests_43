import requests
from src.config.api_constants import api_config


def test_basic_auth_success():
    session = requests.Session()
    response = session.post(
        f"{api_config.BASE_URL}/api/v1/login/access-token",
        data=api_config.AUTH_DATA, headers=api_config.AUTH_HEADERS
    )

    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    access_token = response.json().get("access_token")
    assert access_token, "No access_token found"

    print(f"✅ Авторизация прошла успешно. Токен: {access_token[:10]}...")
