
from playwright.sync_api import Page, expect

def navigate_to_cart(page: Page):
    page.hover(selector='.nav-link[href="/headsets"]')
    page.click(selector='a[href="/headsets/oculus-quest"]')
    page.click(selector='.btn[data-test="add-to-cart"]')
    expect(page).to_have_url('https://store.playstation.com/en-ca/checkout')

def verify_removing_from_cart(page: Page):
    page.click(selector='.btn[data-test="remove-item"]')
    expect(page).to_have_text('div[data-test="cart-empty"]', 'Your cart is empty')

def verify_reading_item_to_cart(page: Page):
    page.click(selector='.btn[data-test="add-to-cart"]')
    expect(page).to_have_text('div[data-test="cart-item-count"]', '1')

def select_a_shipping_country(page: Page):
    page.select_option(selector='select[name="country"]', value='CA')
    expect(page).to_have_text('span[data-test="country-name"]', 'Canada')

def verify_clicking_checkout_loads_checkout_page(page: Page):
    page.click(selector='.btn[data-test="checkout-button"]')
    expect(page).to_have_url('https://store.playstation.com/en-ca/checkout')

def enter_personal_details(page: Page):
    page.fill(selector='input[name="firstName"]', value='Name')
    page.fill(selector='input[name="lastName"]', value='Last Name')
    page.fill(selector='input[name="phoneNumber"]', value='123412341')
    page.fill(selector='input[name="address"]', value='1234 Address St')
    page.fill(selector='input[name="city"]', value='Highlands')
    page.select_option(selector='select[name="state"]', value='BC')
    page.fill(selector='input[name="zipCode"]', value='V9B 0K7')
    page.fill(selector='input[name="email"]', value='test@yahoo.com')
    expect(page).to_be_enabled('button[data-test="continue-button"]')