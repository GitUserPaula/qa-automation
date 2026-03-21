# pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")
        self.success_msg = page.locator("#flash.success")
        self.secure_header = page.locator("h2")
        self.error_msg = page.locator(".flash.error")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def is_logged_in(self) -> bool:
        return self.page.url == "https://the-internet.herokuapp.com/secure"

    def get_header(self) -> str:
        expect(self.secure_header).to_be_visible()
        return self.secure_header.text_content().strip()
    
    def get_success_message(self) -> str:
        expect(self.success_msg).to_be_visible()
        return self.success_msg.text_content().strip()

    def get_error_message(self) -> str:
        error_locator = self.page.locator(".flash.error")
        expect(error_locator).to_be_visible()
        return error_locator.text_content().strip()