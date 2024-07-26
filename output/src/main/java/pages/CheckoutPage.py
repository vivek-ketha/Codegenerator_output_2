
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_first_name(self, first_name: str) -> None:
        self.page.fill("input[name='firstName']", first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.page.fill("input[name='lastName']", last_name)

    def enter_phone_number(self, phone: str) -> None:
        self.page.fill("input[name='phoneNumber']", phone)

    def enter_address(self, address: str) -> None:
        self.page.fill("input[name='address1']", address)

    def enter_city(self, city: str) -> None:
        self.page.fill("input[name='city']", city)

    def select_state(self, state: str) -> None:
        self.page.select_option("select._296s._47p_", value=state)

    def enter_zipcode(self, zipcode: str) -> None:
        self.page.fill("input[name='postalCode']", zipcode)

    def enter_email(self, email: str) -> None:
        self.page.fill("input[name='email']", email)

    def refresh(self) -> None:
        self.page.reload()

    def is_error_container_displayed(self) -> bool:
        return expect(self.page.locator("//div[@class=' _64f3'][contains(text(), 'Please specify a valid email')]")).is_visible()

    def is_continue_button_enabled(self) -> bool:
        return expect(self.page.locator("input[name='submit']")).is_visible()