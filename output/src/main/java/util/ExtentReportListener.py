from playwright.sync_api import Playwright, sync_playwright

def test_my_app(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:5500/index.html")
    page.screenshot(path="example.png")
    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_my_app(playwright)