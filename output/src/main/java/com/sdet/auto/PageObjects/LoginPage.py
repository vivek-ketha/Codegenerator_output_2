```
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    txt_username = "#username"
    txt_password = "
    btn_login = ".fa.fa-2x.fa-sign-in"
    lbl_message = "#flash"

    def enter_credentials(self, user_id: str, password: str):
        self.page.fill(self.txt_username, user_id)
        self.page.fill(self.txt_password, password)
        self.page.click(self.btn_login)

    def verify_message(self, expected_msg: str):
        actual_msg = self.page.locator(self.lbl_message).text_content()
        return expected_msg in actual_msg
```