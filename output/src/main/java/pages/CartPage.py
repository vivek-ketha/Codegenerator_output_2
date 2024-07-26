
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    async def remove_item_from_cart(self):
        await self.page.click("button:has-text('Remove')")

    async def is_item_removed(self) -> bool:
        return await expect(self.page).to_have_text("div.empty-cart-message", "Your cart is empty.").is_visible()

    async def add_item_to_cart_again(self):
        await self.page.click("button:has-text('Add to cart')")

    async def is_item_added(self) -> bool:
        return await expect(self.page).to_have_text("div.product-details").is_visible()

    async def select_country(self, country: str):
        await self.page.select_option("select#shippingCountry", country)
        await expect(self.page.locator("select#shippingCountry")).to_have_attribute("value", country)

    async def selected_country(self) -> str:
        return await self.page.locator("select#shippingCountry").get_attribute("value")

    async def click_checkout_button(self):
        await self.page.click("button:has-text('Checkout')")

    async def is_checkout_page_loaded(self) -> bool:
        await expect(self.page).to_have_text("span.checkout-header", "Checkout")
        return await expect(self.page).to_have_css("div.checkout-content").is_visible()