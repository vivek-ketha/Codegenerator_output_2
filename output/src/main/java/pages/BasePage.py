
from playwright.sync_api import Playwright, sync_playwright

def test_base_page():
    with sync_playwright() as playwright:
        chrome = playwright.chromium
        browser = chrome.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.oculus.com/")
        browser.close()