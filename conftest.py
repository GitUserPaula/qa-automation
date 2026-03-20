# conftest.py

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def login_page(browser):
    page = browser.new_page()
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate()
    yield login
    page.close()

def pytest_html_report_title(report):
    report.title = "QA Automation Execution Report - Playwright"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<p>Project: SauceDemo Automation</p>"])
    prefix.extend([f"<p>Tester: Paula (Senior QA)</p>"])