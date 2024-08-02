  Here's how you can convert the code to Playwright:

```python
from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    async def enter_first_name(self, first_name: str) -> None:
        await self.page.fill("input[name='firstName']", first_name)

    async def enter_last_name(self, last_name: str) -> None:
        await self.page.fill("input[name='lastName']", last_name)

    async def enter_phone_number(self, phone: str) -> None:
        await self.page.fill("input[name='phoneNumber']", phone)

    async def enter_address(self, address: str) -> None:
        await self.page.fill("input[name='address1']", address)

    async def enter_city(self, city: str) -> None:
        await self.page.fill("input[name='city']", city)

    async def select_state(self, state: str) -> None:
        await self.page.select_option("select._296s._47p_", state)

    async def enter_zipcode(self, zipcode: str) -> None:
        await self.page.fill("input[name='postalCode']", zipcode)

    async def enter_email(self, email: str) -> None:
        await self.page.fill("input[name='email']", email)

    async def refresh(self) -> None:
        await self.page.reload()

    async def is_error_container_displayed(self) -> bool:
        error_container = await self.page.locator("div._64f3").filter(has_text="Please specify a valid email").first()
        return await error_container.is_visible()

    async def is_continue_button_enabled(self) -> bool:
        continue_button = await self.page.locator("button[name='submit']").first()
        return await continue_button.is_enabled()
```