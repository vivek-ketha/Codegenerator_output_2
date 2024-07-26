
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    async def enter_first_name(self, first_name: str) -> None:
        await self.page.locator("input[name='firstName']").fill(first_name)

    async def enter_last_name(self, last_name: str) -> None:
        await self.page.locator("input[name='lastName']").fill(last_name)

    async def enter_phone_number(self, phone: str) -> None:
        await self.page.locator("input[name='phoneNumber']").fill(phone)

    async def enter_address(self, address: str) -> None:
        await self.page.locator("input[name='address1']").fill(address)

    async def enter_city(self, city: str) -> None:
        await self.page.locator("input[name='city']").fill(city)

    async def select_state(self, state: str) -> None:
        await self.page.locator("select[name='stateProvince'] >> text=" + state).click()

    async def enter_zipcode(self, zipcode: str) -> None:
        await self.page.locator("input[name='postalCode']").fill(zipcode)

    async def enter_email(self, email: str) -> None:
        await self.page.locator("input[name='email']").fill(email)

    async def refresh(self) -> None:
        await self.page.reload()

    async def is_error_container_displayed(self) -> bool:
        return await self.page.locator("div[class='_64f3'] >> text=Please specify a valid email").is_visible()

    async def is_continue_button_enabled(self) -> bool:
        return await self.page.locator("button[name='submit']").is_enabled()