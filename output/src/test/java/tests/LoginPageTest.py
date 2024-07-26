
from playwright.sync_api import Playwright, sync_playwright

def test_login_page(page):
    page.goto("https://example.com/login")
    page.click("text=Log In or Sign Up")
    page.click("text=Sign in")
    login_page = LoginPage(page)
    login_page.type_username("InvalidEmail@gmail.com")
    login_page.type_password("")
    login_page.click_sign_in()
    assert login_page.error_container_displayed()
    login_page.type_username("testuser@yahoo.com")
    login_page.type_password("")
    login_page.click_sign_in()
    assert login_page.error_container_displayed()
    login_page.type_username("username")
    login_page.type_password("")
    login_page.click_sign_in()
    assert login_page.verify_new_page()

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.click(selector)

    def type(self, selector, text):
        self.page.type(selector, text)

    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector)

class HomePage(BasePage):
    def click_log_in_link(self):
        self.click("text=Log In or Sign Up")

    def click_signin_link(self):
        self.click("text=Sign in")

class LoginPage(BasePage):
    def type_username(self, username):
        self.type("#username", username)

    def type_password(self, password):
        self.type("#password", password)

    def click_sign_in(self):
        self.click("#sign-in")

    def error_container_displayed(self):
        try:
            self.wait_for_element("#error-container")
            return True
        except:
            return False

    def verify_new_page(self):
        return self.page.url == "https://example.com/home"

with sync_playwright() as playwright:
    for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:
        with browser_type.launch() as browser:
            with browser.new_context() as context:
                for page in browser.new_pages():
                    test_login_page(page)