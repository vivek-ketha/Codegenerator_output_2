
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    txtUsername = "#username"
    txtPassword = "
    btnLogin = ".fa.fa-2x.fa-sign-in"
    lblMessage = "#flash"

    def enter_credentials(self, user_id: str, password: str):
        self.page.fill(self.txtUsername, user_id)
        self.page.fill(self.txtPassword, password)
        self.page.click(self.btnLogin)

    def verify_message(self, test_assert, expected_msg: str):
        actual_msg = self.page.text_content(self.lblMessage)
        test_assert.set_pass(LoggingLibrary.CompareResultContains(actual_msg, expected_msg))