
from playwright.sync_api import Playwright, Page, Browser, BrowserContext

def setup(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return browser

def teardown(browser: Browser) -> None:
    browser.close()

browser = setup(playwright)
page = browser.new_page()
page.goto("https://www.oculus.com/")
teardown(browser)