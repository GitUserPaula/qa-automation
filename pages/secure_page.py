# pages/secure_page.py

from playwright.sync_api import Page, expect

class SecurePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/secure"
        self.welcome_message = page.locator("h2")
        self.logout_button = page.locator("a[href='/logout']")

    def navigate_with_token(self, token: str):
        self.page.goto(f"{self.url}?token={token}")

    def get_welcome_text(self) -> str:
        expect(self.welcome_message).to_be_visible()
        return self.welcome_message.text_content().strip()

    def logout(self):
        self.logout_button.click()