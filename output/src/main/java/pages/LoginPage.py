from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page): # create a constructor and pass the page instance
        self.page = page

    async def type_username(self, username: str): #pass a parameter so we don't hardcode values in the object class.
        await self.page.fill("#email", username)

    async def type_password(self, password: str):
        await self.page.fill("#password", password)

    async def click_sign_in(self):
        await self.page.click("#sign_in")

    async def error_container_displayed(self) -> bool:
        error_container = await self.page.query_selector(".bxInputControl.bxInputControl--error")
        return await error_container.is_visible()

    async def verify_new_page(self) -> bool:
        await self.page.wait_for_url("https://www.oculus.com/")
        return "Oculus | VR Headsets & Equipment" in await self.page.title()