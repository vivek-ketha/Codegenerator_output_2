
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        return self.page.title()

    def get_logo(self) -> bool:
        return self.page.locator("._2v0_").is_visible()

    def click_log_in_link(self):
        self.page.locator("a:has-text('Log In or Sign Up')").click()

    def click_signin_link(self):
        self.page.locator("a#u_0_1v:has-text('Sign in')").click()

    def hover_over_community_tab(self):
        self.page.locator("#u_0_17").hover()

    def click_forums_tab(self):
        self.page.locator("#u_0_17").click()

    def switch_tabs(self):
        tabs = self.page.context.pages
        self.page.context.switch_to_page(tabs[1])

    def hover_over_headsets_tab(self):
        self.page.locator("#u_0_x").hover()

    def headsets_dropdown_results(self):
        return self.page.locator("div.modal__button-wrapper-128").all_text_contents()

    def click_oculus_quest(self):
        self.page.locator("#u_0_10").click()

    def add_to_cart(self):
        self.page.locator("button._8166._4pg_._3hmq._4phk._4ph1:has-text('Buy Now')").click()
        self.page.locator("div>.modal__button-wrapper-128").click()

    def is_cart_page_loaded(self) -> bool:
        return expect(self.page.locator("._4ju3._4pg_._3hmq._4phk")).is_visible()