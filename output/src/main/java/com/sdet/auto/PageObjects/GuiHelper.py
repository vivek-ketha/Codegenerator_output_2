```
from playwright.sync_api import Page, sync_playwright

class GuiHelper:
    @staticmethod
    def open_web_browser():
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()

    @staticmethod
    def close_web_browser():
        browser.close()
```