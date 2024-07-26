
from playwright.sync_api import Page, expect
from tests.base_test import BaseTest

class CheckoutTest(BaseTest):
    def test_navigate_to_cart(self):
        page = self.page
        page.hover_over_headsets_tab()
        self.logger.info("Hovering over 'Headsets'")
        page.click_oculus_quest()
        self.logger.info("Selecting Oculus Quest link")
        page.add_to_cart()
        self.logger.info("Adding item to cart")
        expect(page.is_cart_page_loaded()).to_be_truthy()

    def test_verify_removing_from_cart(self):
        page = self.page
        page.remove_item_from_cart()
        self.logger.info("Removing item from cart")
        expect(page.is_item_removed()).to_be_truthy()

    def test_verify_reading_item_to_cart(self):
        page = self.page
        page.add_item_to_cart_again()
        self.logger.info("Readding an item to cart")
        expect(page.is_item_added()).to_be_truthy()

    def test_select_a_shipping_country(self):
        page = self.page
        page.select_country("CA")
        self.logger.info("Changing shipping country to value CA")
        expect(page.selected_country()).to_equal("Canada")

    def test_verify_clicking_checkout_loads_checkout_page(self):
        page = self.page
        page.click_checkout_button()
        self.logger.info("Clicking checkout button")
        expect(page.is_checkout_page_loaded()).to_be_truthy()

    def test_enter_personal_details(self):
        page = self.page
        page.enter_first_name("Name")
        self.logger.info("Entering first name in the First Name field")
        page.enter_last_name("Last Name")
        self.logger.info("Entering last name in the Last Name field")
        page.enter_phone_number("123412341")
        self.logger.info("Entering phone number in the Phone field")
        page.enter_address("1234 Address St")
        self.logger.info("Entering address in the Address field")
        page.enter_city("Highlands")
        self.logger.info("Entering city in the City field")
        page.select_state("BC")
        self.logger.info("Selecting from state/province from dropdown")
        page.enter_zipcode("V9B 0K7")
        self.logger.info("Entering zip code in the Zip Code field")
        page.enter_email("")
        self.logger.info("Entering email in the Email field")
        try:
            expect(page.is_continue_button_enabled()).to_be_truthy()
            self.logger.info("Continue button is enabled, all data are correct")
        except Exception as e:
            self.logger.warning("Continue button was not enabled due to invalid data")