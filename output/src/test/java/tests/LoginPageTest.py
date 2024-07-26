
from playwright.sync_api import Page, expect

def navigate_to_login_page(page: Page):
    page.goto("https://www.example.com")
    page.click("text=Log In or Sign Up")
    page.click("text=Sign in")

def verify_invalid_login_credentials(page: Page):
    page.type("#username", "InvalidEmail@gmail.com")
    page.type("#password", "")
    page.click("text=Sign in")
    expect(page).to_have_text("Invalid username or password")

def verify_login(page: Page, username: str, password: str):
    page.type("#username", username)
    page.type("#password", password)
    page.click("text=Sign in")
    expect(page).to_have_text("Welcome, " + username)