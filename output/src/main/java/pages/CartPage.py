from playwright.sync_api import Page, Selectors

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.selectors = Selectors(page)

    def remove_item_from_cart(self) -> None:
        self.page.locator("button:has-text('Remove')").click()

    def is_item_removed(self) -> bool:
        return self.page.locator("div._1uv2 h4:has-text('Your cart is empty.')").is_visible()

    def add_item_to_cart_again(self) -> None:
        self.page.locator("div:nth-child(9) >> form >> button").click()

    def is_item_added(self) -> bool:
        return self.page.locator("div._4rzp").is_visible()

    def select_country(self, country: str) -> None:
        select = Selectors(self.page).get("select#shippingCountry")
        select.select_option(value=country)
        select.wait_for(state="visible")

    def selected_country(self) -> str:
        select = Selectors(self.page).get("select#shippingCountry")
        return select.get_attribute("value")

    def click_checkout_button(self) -> None:
        self.page.locator("button._4ju3._4pg_._3hmq._4phk").click()

    def is_checkout_page_loaded(self) -> bool:
        self.page.locator("div._33ng._663y.clearfix").wait_for(state="visible")
        return self.page.locator("span._45mg:has-text('Checkout')").is_visible()