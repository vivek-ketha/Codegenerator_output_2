
from playwright.sync_api import Page, Selectors

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.remove_option = Selectors.xpath("//button[contains(text(), 'Remove')]")
        self.empty_cart_message = Selectors.xpath("//div[@class='_1uv2']/h4[contains(text(), 'Your cart is empty.')]")
        self.add_product_to_cart = Selectors.xpath("//div[9]//div[1]//form[1]//button[1]")
        self.product_details = Selectors.css_selector("._4rzp")
        self.shipping_country_dropdown = Selectors.css_selector("#shippingCountry")
        self.checkout_button = Selectors.css_selector("._4ju3._4pg_._3hmq._4phk")
        self.checkout_header = Selectors.xpath("//span[@class='_45mg'][contains(text(), 'Checkout')]")
        self.checkout_page_content = Selectors.css_selector("._33ng._663y.clearfix")

    def remove_item_from_cart(self):
        self.page.click(self.remove_option)

    def is_item_removed(self):
        return self.page.wait_for_selector(self.empty_cart_message).is_visible()

    def add_item_to_cart_again(self):
        self.page.click(self.add_product_to_cart)

    def is_item_added(self):
        return self.page.wait_for_selector(self.product_details).is_visible()

    def select_country(self, country):
        select = Selectors.select_by_value(self.shipping_country_dropdown, country)
        self.page.select_option(self.shipping_country_dropdown, select)
        self.page.wait_for_selector(self.shipping_country_dropdown, state="visible", has_value=country)

    def selected_country(self):
        return self.page.select_option(self.shipping_country_dropdown).get_attribute("value")

    def click_checkout_button(self):
        self.page.click(self.checkout_button)

    def is_checkout_page_loaded(self):
        self.page.wait_for_selector(self.checkout_page_content, state="visible")
        return self.page.wait_for_selector(self.checkout_header).is_visible()