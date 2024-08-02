from playwright.sync_api import Page, Selectors

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstNameField = Selectors.css("[name='firstName']")
        self.lastNameField = Selectors.css("[name='lastName']")
        self.phoneField = Selectors.css("[name='phoneNumber']")
        self.addressField = Selectors.css("[name='address1']")
        self.cityField = Selectors.css("[name='city']")
        self.stateProvinceDropdown = Selectors.css("._296s._47p_")
        self.zipcodeField = Selectors.css("[name='postalCode']")
        self.emailField = Selectors.css("[name='email']")
        self.emailOptInCheckbox = Selectors.css("[name='optInAsGuest']")
        self.continueToPaymentButton = Selectors.css("[name='submit']")
        self.errorContainer = Selectors.css("//div[@class=' _64f3'][contains(text(), 'Please specify a valid email')]")

    def enter_first_name(self, first_name: str) -> None:
        self.firstNameField.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.lastNameField.fill(last_name)

    def enter_phone_number(self, phone: str) -> None:
        self.phoneField.fill(phone)

    def enter_address(self, address: str) -> None:
        self.addressField.fill(address)

    def enter_city(self, city: str) -> None:
        self.cityField.fill(city)

    def select_state(self, state: str) -> None:
        self.stateProvinceDropdown.select_option(value=state)

    def enter_zipcode(self, zipcode: str) -> None:
        self.zipcodeField.fill(zipcode)

    def enter_email(self, email: str) -> None:
        self.emailField.fill(email)

    def is_error_container_displayed(self) -> bool:
        return self.errorContainer.is_visible()

    def is_continue_button_enabled(self) -> bool:
        return self.continueToPaymentButton.is_enabled()