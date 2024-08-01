```
from playwright.sync_api import Page

class Navigation:
    def __init__(self, page: Page):
        self.page = page

    def nav_to_web_page_under_test(self):
        self.page.goto(ConfigSettings.get_web_url())
```