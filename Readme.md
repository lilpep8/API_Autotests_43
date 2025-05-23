## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение:
   ```bash
    python -m venv .venv
    # Activate:
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows
3. pip install -r requirements.txt
4. Создайте .env в директории FastApi файл и вставьте свои данные, которые указали при регистрации
    ```bash
    API_EMAIL = your_email@example.com
    API_PASSWORD = your_password
5. Создайте test_auth.py в директории FastApi файл и вставьте токен, который получили при авторизации
   * Открой сайт: https://dashboard.pomidor-stage.ru
   * Нажмите `F12` или перейдите в `DevTools`.
   * Перейдите во вкладку `→` **Network** перед вводом логина и пароля.
   * Выполните вход с вашим логином/паролем .
   * Найдите запрос к `/api/v1/login/access-token`.
   * Ответ (Response): JSON, содержащий поле access_token
   ```bash
    token = { "access_token": "your_example_token",
    "token_type": "bearer"}

6. Перейдите в директорию tests 
    ```bash
    cd FastApi/tests/
7. Запустите тесты
    ```bash
   python -m pytest test_items.py -v -s
   ```
   ```bash
   python -m pytest test_security.py -v -s
   ```
   ```bash
   python -m pytest test_negative_cases.py -v -s
   ```
## Структура проекта
    FastApi/
    ├── .env                             # Локальные переменные (ваши учетные данные)
    ├── .gitignore                       # Игнорируемые файлы
    ├── requirements.txt                 # Зависимости
    ├── tests/
    │   ├── test_auth.py                 # Токен авторизации
    │   ├── test_items.py                # Тесты для /items
    │   ├── test_security.py             # Тесты на безопасность
    │   ├── test_negative_cases.py       # Негативые тест кейсы
    │   ├── conftest.py                  # Фикстуры
    ├── config/
    │   ├── constants.py                 # Настройки API (использует .env)