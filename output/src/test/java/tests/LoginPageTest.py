from playwright.sync_api import Page, expect

def test_login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("text=Log In").click()
    page.locator("text=Sign in").click()
    test_data = [
        ("InvalidEmail@gmail.com", "testing123"),  # Invalid email, correct password
        ("testuser@yahoo.com", "InvalidPassword2"),  # Correct email, Invalid password
    ]
    for username, password in test_data:
        page.locator("#user-name").fill(username)
        page.locator("#password").fill(password)
        page.locator("text=Sign In").click()
        expect(page.locator(".error-message-container")).to_be_visible()
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("")
    page.locator("text=Sign In").click()
    expect(page.locator(".product_label")).to_be_visible()