from playwright.sync_api import Page, Selectors

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.remove_option = page.locator("//button[contains(text(), 'Remove')]")
        self.empty_cart_message = page.locator("//div[@class='_1uv2']/h4[contains(text(), 'Your cart is empty.')]")
        self.add_product_to_cart = page.locator("//div[9]//div[1]//form[1]//button[1]")
        self.product_details = page.locator("._4rzp")
        self.shipping_country_dropdown = page.locator("#shippingCountry")
        self.checkout_button = page.locator("._4ju3._4pg_._3hmq._4phk")
        self.checkout_header = page.locator("//span[@class='_45mg'][contains(text(), 'Checkout')]")
        self.checkout_page_content = page.locator("._33ng._663y.clearfix")

    def remove_item_from_cart(self):
        self.remove_option.click()

    def is_item_removed(self):
        return self.empty_cart_message.is_visible()

    def add_item_to_cart_again(self):
        self.add_product_to_cart.click()

    def is_item_added(self):
        return self.product_details.is_visible()

    def select_country(self, country):
        self.shipping_country_dropdown.select_option(value=country)
        self.shipping_country_dropdown.wait_for_value(country)

    def selected_country(self):
        return self.shipping_country_dropdown.get_attribute("value")

    def click_checkout_button(self):
        self.checkout_button.click()

    def is_checkout_page_loaded(self):
        self.checkout_page_content.wait_for()
        return self.checkout_header.is_visible()