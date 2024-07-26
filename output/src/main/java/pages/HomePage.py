
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    oculus_logo = Page.locator("_2v0_")
    signin_link = Page.locator("a:has-text('Log In or Sign Up')")
    signin_button = Page.locator("a#u_0_1v:has-text('Sign in')")
    headsets_tab = Page.locator("#u_0_x")
    apps_games_tab = Page.locator("#u_0_y")
    community_tab = Page.locator("#u_0_15")
    support_tab = Page.locator("#u_0_17")
    oculus_quest = Page.locator("#u_0_10")
    buy_now_button = Page.locator("button._8166._4pg_._3hmq._4phk._4ph1:has-text('Buy Now')")
    one_twenty_eight_gb = Page.locator("div>.modal__button-wrapper-128")
    checkout_button = Page.locator("._4ju3._4pg_._3hmq._4phk")
    navigation_links = Page.locator("._2xvt._wjv._2xvr")
    containers = Page.locator("._2xvt._wjv._2xvr/span/a[contains(@data-testid, 'navlink-')]")
    headsets_dropdown = Page.locator("div._2xvy._8yxy._2xvr._7ujs._8yxz")
    headsets_dropdown_results = Page.locator("div._2xvy._8yxy._2xvr._7ujs._8yxz/span/a[contains(@data-testid, 'navlink-')]")
    forums_tab = Page.locator("#u_0_17")

    def get_title(self) -> str:
        return self.page.title()

    def get_logo(self) -> bool:
        return self.oculus_logo.is_visible()

    def click_log_in_link(self):
        self.signin_link.click()

    def click_signin_link(self):
        self.signin_button.click()

    def hover_over_community_tab(self):
        self.community_tab.hover()

    def click_on_forums_tab(self):
        self.forums_tab.click()

    def switch_tabs(self):
        tabs = self.page.context.pages
        self.page.context.switch_to_page(tabs[1])

    def hover_over_headsets_tab(self):
        self.headsets_tab.hover()

    def headsets_dropdown_results(self):
        return self.headsets_dropdown.query_selector_all(self.headsets_dropdown_results)

    def click_oculus_quest(self):
        self.oculus_quest.click()

    def add_to_cart(self):
        self.buy_now_button.click()
        self.one_twenty_eight_gb.click()

    def is_cart_page_loaded(self) -> bool:
        return self.checkout_button.is_visible()