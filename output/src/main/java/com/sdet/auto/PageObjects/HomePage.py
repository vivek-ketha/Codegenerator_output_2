```
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def txt_header(self):
        return self.page.locator(".heading")

    @property
    def link_forget_password(self):
        return self.page.locator("[href='/forgot_password']")

    @property
    def link_form_authentication(self):
        return self.page.locator("[href='/login']")

    def click_forget_password(self):
        self.link_forget_password.click()

    def click_form_authentication(self):
        self.link_form_authentication.click()

    def verify_on_home_page(self):
        header_text = self.txt_header.text_content()
        assert header_text == "Welcome to the-internet"
```