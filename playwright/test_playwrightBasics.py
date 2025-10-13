import time
from playwright.sync_api import Page, expect, Playwright
import pytest

# Optional test, still skipped
@pytest.mark.skip  
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

# Optional shortcut test
@pytest.mark.skip    
def test_playwrightShortcut(page: Page):
    print("Success")
    page.goto("https://rahulshettyacademy.com")

# ✅ Main test
def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    print("Success")
    time.sleep(5)

#firfoxBrowser 
def test_coreLocators(playwright: Playwright):
    firefoxbrowser = playwright.firefox.launch(headless=False)
    context = firefoxbrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    print("Success")
    time.sleep(5)