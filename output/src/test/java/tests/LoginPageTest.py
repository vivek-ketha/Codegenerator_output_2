
from playwright.sync_api import Page, expect
from tests.base_test import BaseTest


class LoginPageTest(BaseTest):
    def test_navigate_to_login_page(self):
        self.home_page.click_log_in_or_sign_up_button()
        self.logger.info("Clicking 'Log In or Sign Up' button")
        self.home_page.click_sign_in_link()
        self.logger.info("Clicking the 'Sign in' link")

    def test_verify_invalid_login_credentials(self):
        invalid_email = "InvalidEmail@gmail.com"
        correct_password = ""
        self.login_page.type_username(invalid_email)
        self.logger.info("Entering invalid username")
        self.login_page.type_password(correct_password)
        self.logger.info("Entering invalid password")
        self.login_page.click_sign_in_button()
        self.logger.info("Clicking Sign in button")
        expect(self.login_page.error_container).to_be_visible()
        self.logger.info("Log in with invalid credentials failed")

    def test_verify_login(self):
        username = "testuser@yahoo.com"
        password = ""
        self.login_page.type_username(username)
        self.logger.info("Entering valid username")
        self.login_page.type_password(password)
        self.logger.info("Entering valid password")
        self.login_page.click_sign_in_button()
        self.logger.info("Clicking Sign in button")
        expect(self.login_page.new_page).to_be_visible()