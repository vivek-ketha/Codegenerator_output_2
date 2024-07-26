
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#email")
        self.password_field = page.locator("#password")
        self.sign_in_button = page.locator("#sign_in")
        self.oculus_logo = page.locator("._2v0_")
        self.error_container = page.locator(".bxInputControl.bxInputControl--error")

    async def type_username(self, username: str) -> None:
        await self.username_field.clear()
        await self.username_field.type(username)

    async def type_password(self, password: str) -> None:
        await self.password_field.clear()
        await self.password_field.type(password)

    async def click_sign_in(self) -> None:
        await self.sign_in_button.click()

    async def error_container_displayed(self) -> bool:
        return await expect(self.error_container).to_be_visible().is_visible()

    async def verify_new_page(self) -> bool:
        await expect(self.page).to_have_url("https://www.oculus.com/")
        return await self.page.title().contains("Oculus | VR Headsets & Equipment")