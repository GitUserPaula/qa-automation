# tests/test_login.py

import pytest
import csv
import os
from pages.login_page import LoginPage

def get_test_data():
    data = []
    file_path = os.path.join("data", "test_data.csv")
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Saltar encabezado
        for row in reader:
            if row:
                username, password, expected = row
                data.append((username, password, expected.strip()))
    return data

@pytest.mark.parametrize("username,password,expected", get_test_data())
def test_login_scenarios(login_page: LoginPage, username, password, expected):
    login_page.login(username, password)
    
    if expected == "Success":
        message = login_page.get_success_message()
        assert "you logged into a secure area" in message.lower()
    else:
        message = login_page.get_error_message()
        message_lower = message.lower()
        if len(username) < 5 or not username.isalnum():
            assert "username is invalid" in message_lower
        else:
            assert "password is invalid" in message_lower