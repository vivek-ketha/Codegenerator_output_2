
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.oculus.com/"

    def setup(self):
        self.page.goto(self.url)

    def teardown(self):
        self.page.close()