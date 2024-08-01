```
from playwright.sync_api import Page, Browser

class EmailSentPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_email_sent(self, expected_msg: str) -> None:
        actual_msg = self.page.locator(txtMessage).inner_text()
        assert actual_msg == expected_msg
```