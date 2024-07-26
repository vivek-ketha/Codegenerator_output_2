
from playwright.sync_api import Playwright, Page

class BasePage:
    def __init__(self, playwright: Playwright, page: Page):
        self.playwright = playwright
        self.page = page
        self.url = "https://www.oculus.com/"

    def setup(self):
        self.page.set_viewport_size(width=1280, height=800)
        self.page.goto(self.url)

    def tear_down(self):
        self.playwright.close()