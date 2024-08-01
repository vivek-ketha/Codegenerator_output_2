from playwright.sync_api import Page, Selectors

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = Selectors(page)

    def remove_item_from_cart(self):
        self.page.click(self.selectors.button("Remove"))

    def is_item_removed(self) -> bool:
        return self.page.is_visible("text=Your cart is empty.")

    def add_item_to_cart_again(self):
        self.page.click(self.selectors.button("Add to Cart"))

    def is_item_added(self) -> bool:
        return self.page.is_visible(self.selectors.text_content("Product details"))

    def select_country(self, country: str):
        self.page.select_option(self.selectors.select_box("Shipping country"), value=country)

    def selected_country(self) -> str:
        return self.page.get_attribute(self.selectors.select_box("Shipping country"), "value")

    def click_checkout_button(self):
        self.page.click(self.selectors.button("Checkout"))

    def is_checkout_page_loaded(self) -> bool:
        return self.page.is_visible(self.selectors.text_content("Checkout"))