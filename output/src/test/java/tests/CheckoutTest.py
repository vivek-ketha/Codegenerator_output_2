from playwright.sync_api import Page, expect

def navigate_to_cart(page: Page):
    page.hover(selector='.nav-link[href="/headsets"]')
    page.click(selector='.nav-link[href="/headsets/oculus-quest"]')
    page.click(selector='.btn-primary')
    expect(page).to_have_url(
        'https://www.saucedemo.com/cart.html'
    )

def verify_removing_from_cart(page: Page):
    page.click(selector='.btn-danger')
    expect(page).to_have_text(
        'div.alert-warning',
        'Product removed.'
    )

def verify_reading_item_to_cart(page: Page):
    page.click(selector='.btn-primary')
    expect(page).to_have_text(
        'div.alert-success',
        'Product added to cart.'
    )

def select_a_shipping_country(page: Page):
    page.select_option(
        selector='select[name="country"]',
        value='CA'
    )
    expect(page).to_have_text(
        'div.alert-info',
        'Canada'
    )

def verify_clicking_checkout_loads_checkout_page(page: Page):
    page.click(selector='.btn-primary')
    expect(page).to_have_url(
        'https://www.saucedemo.com/checkout-step-one.html'
    )

def enter_personal_details(page: Page):
    page.fill(selector='input[name="firstName"]', value='Name')
    page.fill(selector='input[name="lastName"]', value='Last Name')
    page.fill(selector='input[name="phoneNumber"]', value='123412341')
    page.fill(selector='input[name="address"]', value='1234 Address St')
    page.fill(selector='input[name="city"]', value='Highlands')
    page.select_option(
        selector='select[name="state"]',
        value='BC'
    )
    page.fill(selector='input[name="zip"]', value='V9B 0K7')
    page.fill(selector='input[name="email"]', value='')
    expect(page).to_be_enabled(
        selector='.btn-primary'
    )