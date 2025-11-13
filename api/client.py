# api/client.py
import requests
from typing import Dict

class APIClient:
    def __init__(self):
        self.base_url = "https://the-internet.herokuapp.com"
        self.session = requests.Session()

    def login(self, username: str, password: str) -> Dict:
        url = f"{self.base_url}/authenticate"
        payload = {"username": username, "password": password}
        response = self.session.post(url, json=payload)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON"}