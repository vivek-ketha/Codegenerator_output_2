
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("name=firstName")
        self.last_name_field = page.locator("name=lastName")
        self.phone_field = page.locator("name=phoneNumber")
        self.address_field = page.locator("name=address1")
        self.city_field = page.locator("name=city")
        self.state_province_dropdown = page.locator("css=._296s._47p_")
        self.zipcode_field = page.locator("name=postalCode")
        self.email_field = page.locator("name=email")
        self.email_opt_in_checkbox = page.locator("name=optInAsGuest")
        self.continue_to_payment_button = page.locator("name=submit")
        self.error_container = page.locator("xpath=//div[@class=' _64f3'][contains(text(), 'Please specify a valid email')]")

    def enter_first_name(self, first_name: str) -> None:
        self.first_name_field.clear()
        self.first_name_field.type(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.last_name_field.clear()
        self.last_name_field.type(last_name)

    def enter_phone_number(self, phone: str) -> None:
        self.phone_field.clear()
        self.phone_field.type(phone)

    def enter_address(self, address: str) -> None:
        self.address_field.clear()
        self.address_field.type(address)

    def enter_city(self, city: str) -> None:
        self.city_field.clear()
        self.city_field.type(city)

    def select_state(self, state: str) -> None:
        self.state_province_dropdown.select_option(value=state)

    def enter_zipcode(self, zipcode: str) -> None:
        self.zipcode_field.clear()
        self.zipcode_field.type(zipcode)

    def enter_email(self, email: str) -> None:
        self.email_field.clear()
        self.email_field.type(email)

    def refresh(self) -> None:
        self.page.reload()

    def is_error_container_displayed(self) -> bool:
        return self.error_container.is_visible()

    def is_continue_button_enabled(self) -> bool:
        return self.continue_to_payment_button.is_enabled()