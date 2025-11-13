# tests/test_api_ui.py
import pytest
import responses
import csv
import os
from api.client import APIClient
from pages.login_page import LoginPage  # ← Asegúrate de tener este archivo

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def login_page_instance(browser):  # ← RENOMBRADO
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    yield login_page
    page.close()

def get_credentials():
    data = []
    path = os.path.join("data", "api_credentials.csv")
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Saltar encabezado
        for row in reader:
            if row:
                data.append((row[0], row[1], row[2].strip()))
    return data

@pytest.mark.parametrize("username,password,expected", get_credentials())
@responses.activate
def test_api_to_ui_login(api_client, login_page_instance, username, password, expected):
    # MOCK API
    if expected == "Success":
        responses.post(
            "https://the-internet.herokuapp.com/authenticate",
            json={"token": "abc123xyz"},
            status=200
        )
    else:
        responses.post(
            "https://the-internet.herokuapp.com/authenticate",
            json={"error": "Invalid credentials"},
            status=401
        )

    # UI REAL
    login_page_instance.login(username, password)

    if expected == "Success":
        assert login_page_instance.is_logged_in()
        header = login_page_instance.get_header()
        assert "Secure Area" in header
    else:
        error = login_page_instance.page.locator("#flash.error").text_content()
        assert "invalid" in error.lower()