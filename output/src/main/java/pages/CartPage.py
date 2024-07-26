
from playwright.sync_api import Page, Playwright

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def remove_item_from_cart(self):
        self.page.locator("button:has-text('Remove')").click()

    def is_item_removed(self) -> bool:
        return self.page.locator("div.empty-cart-message:has-text('Your cart is empty.')").is_visible()

    def add_item_to_cart_again(self):
        self.page.locator("form:nth-child(1) > button:nth-child(1)").click()

    def is_item_added(self) -> bool:
        return self.page.locator("div.product-details").is_visible()

    def select_country(self, country: str):
        self.page.locator("select#shippingCountry").select_option(country)

    def selected_country(self) -> str:
        return self.page.locator("select#shippingCountry").get_attribute("value")

    def click_checkout_button(self):
        self.page.locator("button.checkout-button").click()

    def is_checkout_page_loaded(self) -> bool:
        return self.page.locator("div.checkout-page-content").is_visible()