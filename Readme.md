## Установка
1. Клонировать репозиторий
   ```bash
   git clone https://github.com/lilpep8/API_Autotests_43
   ```
2. Создать виртуальное окружение:
   ```bash
    python -m venv .venv
   ```
   ```bash
    source .venv/bin/activate  # Activate Linux/Mac
   ```
   ```bash
    .venv\Scripts\activate     # Activate Windows
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Вставьте свои данные в .env файл, которые использовали при регистрации
    ```bash
    API_EMAIL = your_email@example.com
    API_PASSWORD = your_password
7. Запустите все тесты
   ```bash
   pytest -v -s
   ```
8. Для запуска каждого теста по отдельности, перейдите в директорию tests
    ```bash
   cd tests
   ```
    ```bash
   pytest test_items.py -v -s
   ```
   ```bash
   pytest test_negative_items.py -v -s 
   ```
   ```bash
   pytest test_failed_authorization.py -v -s
   ```
   ```bash
   pytest test_auth.py -v -s
   ```
9. Структура проекта
   ```bash
   📁 src
   ├── 📁 api
   │ └── 📄 api_client.py          # Содержит методы для HTTP запросов к API
   ├── 📁 config
   │ └── 📄 api_constants.py       # Хранит базовые настройки URL, пути к эндпоинтам и тд
   ├── 📁 data_models
   │ └── 📄 models.py              # Хранит Pydantic модели для ответа\запроса валидируемых сущностей Item
   ├── 📁 scenarios                # Логика тестирования на уровне сценариев
   │ ├── 📄 negative_scenarios.py  # Негативные сценарии для невалидных данных
   │ └── 📄 scenario.py            # Позитивные сценарии для CRUD
   └── 📁 utils
   └── 📄 response_validator.py    # Универсальный валидатор моделей и ответов

   📁 tests
   ├── 📄 conftest.py              # Фикстуры для pytest: авторизация, сессия, тестовые данные
   ├── 📄 init.py
   ├── 📄 test_auth.py             # Базовый тест авторизации
   ├── 📄 test_failed_authorization.py # Негативные тесты с авторизацией без токена
   ├── 📄 test_items.py            # CRUD-тесты для эндпоинта /items
   └── 📄 test_negative_items.py   # Негативные тесты с невалидными данными
    ```