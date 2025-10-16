import time
from playwright.sync_api import  Page, Playwright, expect

from utils.api_Base import APIUtils

#api call from browser - api call contact server return back response to browser - browser use response to generate html

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68fe3585f669d6cb0a127f3d")
    

def test_Network(page : Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("jhansy@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abc@12345")
    page.get_by_role("button", name ="Login").click()
    page.get_by_role("button", name ="ORDERS").click()
    page.get_by_role("button", name ="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)
  
  
  
  
def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page =context.new_page()
    #script to inject token in session local storage 
    page.add_init_script("""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.wait_for_timeout(3000) 
    page.get_by_role("button", name ="ORDERS").click()
    expect(page.get_by_text('your Orders')).to_be_visible()
    page.wait_for_timeout(3000)