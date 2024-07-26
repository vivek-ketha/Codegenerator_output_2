
from playwright.sync_api import Playwright, Page

class BasePage:
    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.url = "https://www.oculus.com/"
        self.page.goto(self.url)

    def teardown(self):
        self.browser.close()