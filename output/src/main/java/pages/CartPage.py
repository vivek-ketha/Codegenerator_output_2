
from playwright.sync_api import Page, expect
from playwright.sync_api import SelectLocator

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    remove_option = page.locator("button:has-text('Remove')")
    empty_cart_message = page.locator("div._1uv2 >> h4:has-text('Your cart is empty.')")
    add_product_to_cart = page.locator("div:nth-child(9) >> form >> button:first-child")
    product_details = page.locator("._4rzp")
    shipping_country_dropdown = page.locator("#shippingCountry")
    checkout_button = page.locator("._4ju3._4pg_._3hmq._4phk")
    checkout_header = page.locator("span._45mg:has-text('Checkout')")
    checkout_page_content = page.locator("._33ng._663y.clearfix")

    def remove_item_from_cart(self):
        self.remove_option.click()

    def is_item_removed(self):
        return self.empty_cart_message.is_visible()

    def add_item_to_cart_again(self):
        self.add_product_to_cart.click()

    def is_item_added(self):
        return self.product_details.is_visible()

    def select_country(self, country):
        select = SelectLocator(self.shipping_country_dropdown)
        select.select_option(value=country)
        expect(self.shipping_country_dropdown).to_have_attribute("value", country)

    def selected_country(self):
        select = SelectLocator(self.shipping_country_dropdown)
        return select.get_selected_option().inner_text()

    def click_checkout_button(self):
        self.checkout_button.click()

    def is_checkout_page_loaded(self):
        self.checkout_page_content.wait_for()
        return self.checkout_header.is_visible()