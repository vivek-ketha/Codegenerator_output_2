from playwright.sync_api import Playwright, Page

class BasePage:
    def __init__(self, playwright: Playwright) -> None:
        self.playwright = playwright

    def setup(self):
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def navigate_to_url(self, url: str) -> None:
        self.page.goto(url)

    def teardown(self) -> None:
        self.browser.close()