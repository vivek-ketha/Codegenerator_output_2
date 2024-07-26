
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#email")
        self.password_field = page.locator("#password")
        self.sign_in_button = page.locator("#sign_in")
        self.oculus_logo = page.locator("._2v0_")
        self.error_container = page.locator(".bxInputControl.bxInputControl--error")

    def type_username(self, username: str) -> None:
        self.username_field.fill(username)

    def type_password(self, password: str) -> None:
        self.password_field.fill(password)

    def click_sign_in(self) -> None:
        self.sign_in_button.click()

    def error_container_displayed(self) -> bool:
        return expect(self.error_container).to_be_visible().is_visible()

    def verify_new_page(self) -> bool:
        return expect(self.page).to_have_url("https://www.oculus.com/").is_visible()