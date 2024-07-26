
from playwright.sync_api import Page, expect
from playwright.sync_api import By
from playwright.sync_api import WebDriverWait
from playwright.sync_api import Select

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.wait = WebDriverWait(page, 5)

    firstNameField = By.name("firstName")
    lastNameField = By.name("lastName")
    phoneField = By.name("phoneNumber")
    addressField = By.name("address1")
    cityField = By.name("city")
    stateProvinceDropdown = By.css_selector("._296s._47p_")
    zipcodeField = By.name("postalCode")
    emailField = By.name("email")
    emailOptInCheckbox = By.name("optInAsGuest")
    continueToPaymentButton = By.name("submit")
    errorContainer = By.xpath("//div[@class=' _64f3'][contains(text(), 'Please specify a valid email')]")

    def enterFirstName(self, first_name):
        self.page.locator(self.firstNameField).clear()
        self.page.locator(self.firstNameField).type(first_name)

    def enterLastName(self, last_name):
        self.page.locator(self.lastNameField).clear()
        self.page.locator(self.lastNameField).type(last_name)

    def enterPhoneNumber(self, phone):
        self.page.locator(self.phoneField).clear()
        self.page.locator(self.phoneField).type(phone)

    def enterAddress(self, address):
        self.page.locator(self.addressField).clear()
        self.page.locator(self.addressField).type(address)

    def enterCity(self, city):
        self.page.locator(self.cityField).clear()
        self.page.locator(self.cityField).type(city)

    def selectState(self, state):
        Select(self.page.locator(self.stateProvinceDropdown)).select_by_value(state)

    def enterZipcode(self, zipcode):
        self.page.locator(self.zipcodeField).clear()
        self.page.locator(self.zipcodeField).type(zipcode)

    def enterEmail(self, email):
        self.page.locator(self.emailField).clear()
        self.page.locator(self.emailField).type(email)

    def refresh(self):
        self.page.reload()

    def isErrorContainerDisplayed(self):
        return self.wait.until(lambda: expect(self.page.locator(self.errorContainer)).is_visible())

    def isContinueButtonEnabled(self):
        return self.wait.until(lambda: expect(self.page.locator(self.continueToPaymentButton)).is_enabled())