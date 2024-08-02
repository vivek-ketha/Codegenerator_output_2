from playwright.sync_api import Playwright, Page

def test_base_page(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.oculus.com/")
    context.close()
    browser.close()