from dataclasses import dataclass, field
from dotenv import load_dotenv
import os


load_dotenv()
class EnvConfig:
    EMAIL = os.getenv('API_EMAIL')
    PASSWORD = os.getenv('API_PASSWORD')


@dataclass(frozen=True)
class APIConstants:
    BASE_URL: str = "https://api.pomidor-stage.ru"
    AUTH_HEADERS: dict = field(default_factory=lambda:{
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"}
    )
    AUTH_DATA: dict = field(default_factory=lambda:{
        "username": EnvConfig.EMAIL,
        "password": EnvConfig.PASSWORD,
        "scope": "",
        "client_id": "",
        "client_secret": ""
    })
    API_HEADERS: dict = field(default_factory=lambda:{
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

api_config = APIConstants()






