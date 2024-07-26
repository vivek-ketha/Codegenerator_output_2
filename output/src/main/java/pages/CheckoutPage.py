
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("input[name='firstName']")
        self.last_name_field = page.locator("input[name='lastName']")
        self.phone_field = page.locator("input[name='phoneNumber']")
        self.address_field = page.locator("input[name='address1']")
        self.city_field = page.locator("input[name='city']")
        self.state_province_dropdown = page.locator("select._296s._47p_")
        self.zipcode_field = page.locator("input[name='postalCode']")
        self.email_field = page.locator("input[name='email']")
        self.email_opt_in_checkbox = page.locator("input[name='optInAsGuest']")
        self.continue_to_payment_button = page.locator("button[name='submit']")
        self.error_container = page.locator("div._64f3")

    def enter_first_name(self, first_name: str) -> None:
        self.first_name_field.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.last_name_field.fill(last_name)

    def enter_phone_number(self, phone: str) -> None:
        self.phone_field.fill(phone)

    def enter_address(self, address: str) -> None:
        self.address_field.fill(address)

    def enter_city(self, city: str) -> None:
        self.city_field.fill(city)

    def select_state(self, state: str) -> None:
        self.state_province_dropdown.select_option(value=state)

    def enter_zipcode(self, zipcode: str) -> None:
        self.zipcode_field.fill(zipcode)

    def enter_email(self, email: str) -> None:
        self.email_field.fill(email)

    def refresh(self) -> None:
        self.page.reload()

    def is_error_container_displayed(self) -> bool:
        return self.error_container.is_visible()

    def is_continue_button_enabled(self) -> bool:
        return self.continue_to_payment_button.is_enabled()