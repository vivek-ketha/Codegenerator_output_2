
from playwright.sync_api import Page

def click_forget_password(page: Page):
    page.locator("[href='/forgot_password']").click()

def click_form_authentication(page: Page):
    page.locator("[href='/login']").click()

def verify_on_home_page(page: Page, test_assert):
    header_text = page.locator(".heading").text_content()
    test_assert.set_pass(header_text == "Welcome to the-internet")