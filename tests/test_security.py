from config.constants import BASE_URL


class TestSecurityCases:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_sql_injection(self, sql_injection, auth_session):
        response = auth_session.post(self.endpoint, json=sql_injection)
        assert response.status_code in (200, 201), \
            f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("title") == sql_injection["title"]
        assert data.get("description") == sql_injection["description"]


    def test_xss_attack(self, xss_attack, auth_session):
        response = auth_session.post(self.endpoint, json=xss_attack)
        assert response.status_code in (200, 201), \
            f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("title") == xss_attack["title"]
        assert data.get("description") == xss_attack["description"]