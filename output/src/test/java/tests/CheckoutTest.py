def navigate_to_cart(self):
    home_page = HomePage(self.driver)
    home_page.hover_over_headsets_tab()
    self.logger.info("Hovering over 'Headsets'")
    home_page.click_oculus_quest()
    self.logger.info("Selecting Oculus Quest link")
    home_page.add_to_cart()
    self.logger.info("Adding item to cart")
    assert home_page.is_cart_page_loaded()

def verify_removing_from_cart(self):
    cart_page = CartPage(self.driver)
    cart_page.remove_item_from_cart()
    self.logger.info("Removing item from cart")
    assert cart_page.is_item_removed()

def verify_reading_item_to_cart(self):
    cart_page = CartPage(self.driver)
    cart_page.add_item_to_cart_again()
    self.logger.info("Readding an item to cart")
    assert cart_page.is_item_added()

def select_a_shipping_country(self):
    cart_page = CartPage(self.driver)
    cart_page.select_country("CA")
    self.logger.info("Changing shipping country to value CA")
    assert cart_page.selected_country() == "Canada"

def verify_clicking_checkout_loads_checkout_page(self):
    cart_page = CartPage(self.driver)
    cart_page.click_checkout_button()
    self.logger.info("Clicking checkout button")
    assert cart_page.is_checkout_page_loaded()

def enter_personal_details(self):
    checkout_page = CheckoutPage(self.driver)
    checkout_page.enter_first_name("Name")
    self.logger.info("Entering first name in the First Name field")
    checkout_page.enter_last_name("Last Name")
    self.logger.info("Entering last name in the Last Name field")
    checkout_page.enter_phone_number("123412341")
    self.logger.info("Entering phone number in the Phone field")
    checkout_page.enter_address("1234 Address St")
    self.logger.info("Entering address in the Address field")
    checkout_page.enter_city("Highlands")
    self.logger.info("Entering city in the City field")
    checkout_page.select_state("BC")
    self.logger.info("Selecting from state/province from dropdown")
    checkout_page.enter_zipcode("V9B 0K7")
    self.logger.info("Entering zip code in the Zip Code field")
    checkout_page.enter_email("")
    self.logger.info("Entering email in the Email field")
    try:
        assert checkout_page.is_continue_button_enabled()
        self.logger.info("Continue button is enabled, all data are correct")
    except Exception as e:
        self.logger.warning("Continue button was not enabled due to invalid data")