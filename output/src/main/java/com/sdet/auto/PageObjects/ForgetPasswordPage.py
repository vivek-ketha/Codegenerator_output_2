```
from playwright.sync_api import Page

class ForgetPasswordPage:
    def __init__(self, page: Page):
        self.page = page

    txt_email = "#email"
    btn_retrieve_password = ".icon-2x.icon-signin"

    def enter_email(self, email: str):
        self.page.fill(self.txt_email, email)

    def click_retrieve_button(self):
        self.page.click(self.btn_retrieve_password)
```