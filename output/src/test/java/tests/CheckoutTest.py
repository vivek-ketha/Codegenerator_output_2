
from playwright.sync_api import Page, expect
from playwright.sync_api import expect

def navigate_to_cart(page: Page):
    page.hover_over_selector(".nav-link[href*='headsets']")
    page.click_selector(".nav-link[href*='oculus-quest']")
    page.click_selector(".btn-primary")
    expect(page).to_have_url("https://demo.nopcommerce.com/cart")

def verify_removing_from_cart(page: Page):
    page.click_selector(".btn-danger")
    expect(page).to_have_text(".page-title", "Shopping cart")

def verify_reading_item_to_cart(page: Page):
    page.click_selector(".btn-primary")
    expect(page).to_have_text(".page-title", "Shopping cart")

def select_a_shipping_country(page: Page):
    page.select_option(".country-list", "CA")
    expect(page).to_have_text(".country-list", "Canada")

def verify_clicking_checkout_loads_checkout_page(page: Page):
    page.click_selector(".btn-primary")
    expect(page).to_have_url("https://demo.nopcommerce.com/checkout")

def enter_personal_details(page: Page):
    page.fill_form(".enter-address", {
        "First name": "Name",
        "Last name": "",
        "Phone number": "123412341",
        "Address 1": "1234 Address St",
        "City": "Highlands",
        "Zip/postal code": "V9B 0K7",
        "Email": "test@yahoo.com",
    })
    page.select_option(".state-list", "BC")
    expect(page.locator(".btn-primary")).to_be_enabled()

def checkout_test(page: Page):
    navigate_to_cart(page)
    verify_removing_from_cart(page)
    verify_reading_item_to_cart(page)
    select_a_shipping_country(page)
    verify_clicking_checkout_loads_checkout_page(page)
    enter_personal_details(page)