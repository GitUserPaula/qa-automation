# pages/register_page.py
from playwright.sync_api import Page, expect

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"  # usamos la misma página de login como ejemplo

    def navigate(self):
        self.page.goto(self.url)

    def register_user(self, username: str, password: str):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")