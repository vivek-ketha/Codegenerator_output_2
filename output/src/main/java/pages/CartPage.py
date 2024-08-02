from playwright.sync_api import Page, Selectors

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = Selectors(page, base_url="https://www.amazon.com")

    @property
    def remove_option(self) -> Selectors:
        return self.selectors.button("button:has-text('Remove')")

    @property
    def empty_cart_message(self) -> Selectors:
        return self.selectors.div("_1uv2").h4("h4:has-text('Your cart is empty.')")

    @property
    def add_product_to_cart(self) -> Selectors:
        return self.selectors.button("button:has-text('Add to Cart')")

    @property
    def product_details(self) -> Selectors:
        return self.selectors.div("_4rzp")

    @property
    def shipping_country_dropdown(self) -> Selectors:
        return self.selectors.select("#shippingCountry")

    @property
    def checkout_button(self) -> Selectors:
        return self.selectors.button("_4ju3._4pg_._3hmq._4phk")

    @property
    def checkout_header(self) -> Selectors:
        return self.selectors.span("_45mg:has-text('Checkout')")

    @property
    def checkout_page_content(self) -> Selectors:
        return self.selectors.div("_33ng._663y.clearfix")

    def remove_item_from_cart(self) -> None:
        self.remove_option.click()

    def is_item_removed(self) -> bool:
        return self.empty_cart_message.is_visible()

    def add_item_to_cart_again(self) -> None:
        self.add_product_to_cart.click()

    def is_item_added(self) -> bool:
        return self.product_details.is_visible()

    def select_country(self, country: str) -> None:
        self.shipping_country_dropdown.select_option(value=country)

    def selected_country(self) -> str:
        return self.shipping_country_dropdown.get_attribute("value")

    def click_checkout_button(self) -> None:
        self.checkout_button.click()

    def is_checkout_page_loaded(self) -> bool:
        return self.checkout_header.is_visible()