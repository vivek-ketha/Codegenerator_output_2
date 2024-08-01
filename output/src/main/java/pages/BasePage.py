from playwright.sync_api import Page, Playwright

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def setup(self):
        self.page.goto("https://www.oculus.com/")

    def teardown(self):
        self.page.close()