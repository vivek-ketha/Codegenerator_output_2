from playwright.sync_api import Page, WaitTimeoutError


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def type_username(self, username: str) -> None:
        self.page.fill("input[name='email']", username)

    def type_password(self, password: str) -> None:
        self.page.fill("input[name='password']", password)

    def click_sign_in(self) -> None:
        self.page.click("button[type='submit']")

    def error_container_displayed(self) -> bool:
        try:
            self.page.wait_for_selector(".bxInputControl.bxInputControl--error", state="visible", timeout=10000)
            return True
        except WaitTimeoutError:
            return False

    def verify_new_page(self) -> bool:
        self.page.wait_for_url("https://www.oculus.com/")
        return self.page.title().startswith("Oculus | VR Headsets & Equipment")