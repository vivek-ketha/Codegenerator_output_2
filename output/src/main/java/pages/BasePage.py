
from playwright.sync_api import Page, Playwright

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def setup(self):
        self.page.set_default_timeout(30000)
        self.page.set_default_navigation_timeout(30000)
        self.page.set_viewport_size({"width": 1280, "height": 720})

    def teardown(self):
        self.page.close()