from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    EMAIL = os.getenv('API_EMAIL')
    PASSWORD = os.getenv('API_PASSWORD')


BASE_URL = "https://api.pomidor-stage.ru"

AUTH_HEADERS = {"Content-Type": "application/x-www-form-urlencoded",
           "Accept": "application/json"}

API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

AUTH_DATA = {
    "username": Config.EMAIL,
    "password": Config.PASSWORD,
    "scope": "",
    "client_id": "",
    "client_secret": ""
}
