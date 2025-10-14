from playwright.sync_api import Playwright, expect

from utils.api_Base import APIUtils


def test_web_api(playwright: Playwright):
    firefoxbrowser = playwright.firefox.launch(headless=False)
    context = firefoxbrowser.new_context()
    page = context.new_page()
    
    #creatorder-OrderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    
    
    #login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("jhansy@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abc@12345")
    page.get_by_role("button", name ="Login").click()
    page.get_by_role("button", name ="ORDERS").click()

    
    #orderHistorypage - orderis present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()