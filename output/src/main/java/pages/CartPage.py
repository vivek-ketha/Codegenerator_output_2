
from playwright.sync_api import Page, Locator

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.remove_option = Locator(page, "//button[contains(text(), 'Remove')]")
        self.empty_cart_message = Locator(page, "//div[@class='_1uv2']/h4[contains(text(), 'Your cart is empty.')]")
        self.add_product_to_cart = Locator(page, "//div[9]//div[1]//form[1]//button[1]")
        self.product_details = Locator(page, "._4rzp")
        self.shipping_country_dropdown = Locator(page, "#shippingCountry")
        self.checkout_button = Locator(page, "._4ju3._4pg_._3hmq._4phk")
        self.checkout_header = Locator(page, "//span[@class='_45mg'][contains(text(), 'Checkout')]")
        self.checkout_page_content = Locator(page, "._33ng._663y.clearfix")

    def remove_item_from_cart(self):
        self.remove_option.click()

    def is_item_removed(self) -> bool:
        return self.empty_cart_message.is_visible()

    def add_item_to_cart_again(self):
        self.add_product_to_cart.click()

    def is_item_added(self) -> bool:
        return self.product_details.is_visible()

    def select_country(self, country: str):
        self.shipping_country_dropdown.select_option(value=country)

    def selected_country(self) -> str:
        return self.shipping_country_dropdown.get_attribute("value")

    def click_checkout_button(self):
        self.checkout_button.click()

    def is_checkout_page_loaded(self) -> bool:
        self.checkout_page_content.wait_for()
        return self.checkout_header.is_visible()