from playwright.sync_api import Playwright, sync_playwright

def setup(playwright: Playwright):
    driver = playwright.chromium.launch(headless=False)
    context = driver.new_context()
    page = context.new_page()
    page.goto("https://www.oculus.com/")
    return driver, page

def teardown(driver):
    driver.close()

def test_example(playwright: Playwright):
    driver, page = setup(playwright)
    teardown(driver)

with sync_playwright() as playwright:
    test_example(playwright)