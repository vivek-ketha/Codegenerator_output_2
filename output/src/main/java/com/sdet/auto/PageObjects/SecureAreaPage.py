
from playwright.sync_api import Page
from playwright.sync_api import expect

class SecureAreaPage:

    lbl_message = "#flash"
    btn_logout = ".icon-2x.icon-signout"

    def verify_message(self, page: Page, expected_msg: str) -> None:
        expect(page.locator(self.lbl_message)).to_have_text(expected_msg)

    def click_logout_button(self, page: Page) -> None:
        page.locator(self.btn_logout).click()