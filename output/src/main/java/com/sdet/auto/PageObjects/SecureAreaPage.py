```
from playwright.sync_api import Page

class SecureAreaPage:
    def __init__(self, page: Page):
        self.page = page

    lbl_message = "#flash"
    btn_logout = ".icon-2x.icon-signout"

    def verify_message(self, expected_msg):
        actual_msg = self.page.locator(self.lbl_message).text_content()
        assert expected_msg in actual_msg, f"Expected message '{expected_msg}' not found in actual message '{actual_msg}'"

    def click_logout_button(self):
        self.page.locator(self.btn_logout).click()
```