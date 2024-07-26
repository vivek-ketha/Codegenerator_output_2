
from playwright.sync_api import Page, expect
from playwright.sync_api import Selectors

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    remove_option = Selectors.xpath("//button[contains(text(), 'Remove')]")
    empty_cart_message = Selectors.xpath("//div[@class='_1uv2']/h4[contains(text(), 'Your cart is empty.')]")
    add_product_to_cart = Selectors.xpath("//div[9]//div[1]//form[1]//button[1]")
    product_details = Selectors.css_selector("._4rzp")
    shipping_country_dropdown = Selectors.css_selector("#shippingCountry")
    checkout_button = Selectors.css_selector("._4ju3._4pg_._3hmq._4phk")
    checkout_header = Selectors.xpath("//span[@class='_45mg'][contains(text(), 'Checkout')]")
    checkout_page_content = Selectors.css_selector("._33ng._663y.clearfix")

    def remove_item_from_cart(self):
        self.page.locator(self.remove_option).click()

    def is_item_removed(self):
        return expect(self.page.locator(self.empty_cart_message)).is_visible()

    def add_item_to_cart_again(self):
        self.page.locator(self.add_product_to_cart).click()

    def is_item_added(self):
        return expect(self.page.locator(self.product_details)).is_visible()

    def select_country(self, country):
        Selectors.select_by_value(self.page.locator(self.shipping_country_dropdown), country)
        expect(self.page.locator(self.shipping_country_dropdown)).to_have_attribute("value", country)

    def selected_country(self):
        return Selectors.get_first_selected_option(self.page.locator(self.shipping_country_dropdown)).text_content()

    def click_checkout_button(self):
        self.page.locator(self.checkout_button).click()

    def is_checkout_page_loaded(self):
        expect(self.page.locator(self.checkout_page_content)).to_be_visible()
        return self.page.locator(self.checkout_header).is_visible()