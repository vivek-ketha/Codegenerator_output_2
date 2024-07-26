
from playwright.sync_api import Playwright, sync_playwright

def test_base_page(playwright: Playwright):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.oculus.com/")
        browser.close()