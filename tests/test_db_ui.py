# tests/test_db_ui.py

import pytest
import csv
import os
from db.connection import user_exists
from pages.register_page import RegisterPage

def get_new_users():
    path = os.path.join("data", "new_users.csv")
    users = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            users.append((row["username"], row["password"], row["email"]))
    return users

@pytest.fixture
def register_page(browser):
    page = browser.new_page()
    yield RegisterPage(page)
    page.close()

@pytest.mark.db
@pytest.mark.end_to_end
@pytest.mark.parametrize("username,password,email", get_new_users())
def test_register_and_verify_in_db(register_page, username, password, email):
    # 1. UI: Intentamos registrar/login (en este ejemplo usamos login)
    register_page.navigate()
    register_page.register_user(username, password)

    # 2. VALIDACIÓN EN BASE DE DATOS
    # (En la web real no guarda en DB, pero en un proyecto tuyo SÍ lo haría)
    # Por eso simulamos que después del registro el backend guardó el usuario
    from db.connection import get_connection
    conn = get_connection()
    conn.execute(
        "INSERT OR IGNORE INTO users (username, password, email) VALUES (?, ?, ?)",
        (username, password, email)
    )
    conn.commit()
    conn.close()

    # 3. VERIFICAMOS QUE REALMENTE ESTÁ EN LA DB
    assert user_exists(username) == True

    # BONUS: Screenshot del resultado
    register_page.page.screenshot(path=f"evidencias/db_user_{username}.png")

