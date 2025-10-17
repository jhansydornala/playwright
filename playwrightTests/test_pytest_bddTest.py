
import pytest
from pytest_bdd import given, scenarios, then, when
import pytest_bdd.parsers as parsers

from pageObjects.login import LoginPage
from pageObjects.orderDetails import OrderDetailsPage
from playwrightTests.conftest import user_credentials
from utils.api_BaseFramework import APIUtils

scenarios("features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return{}
"""
@pytest.fixture
def user_credentials():
    return {
        'userEmail': 'jhansy@yopmail.com',
        'password': '1-Abc@12345',
        # add any other needed keys here
    }
"""
@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    """
    user_credentails = {}
    user_credentails['userEmail'] = username
    user_credentails['userPassword'] = password
    """
    user_credentials = {
       'userEmail': username,
       'userPassword': password,
    }
    
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials) 
    shared_data['order_id'] = orderId
    
   # user_credentials = {
    #    'userEmail': username,
    #    'userPassword': password,
   # }
     
    
@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    login_Page = LoginPage(browserInstance)#object for login page class
    login_Page.navigate()  
    shared_data['login_page'] = login_Page
    
@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_Page = shared_data['login_page']
    dashboard_Page = login_Page.login(username, password)
    shared_data['dashboard_page'] = dashboard_Page
    
@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_Page = shared_data['dashboard_page']
    orderHistoryPage = dashboard_Page.selectOrdersNavLink()
    shared_data['orderHistory_page'] = orderHistoryPage
    
@when('select the order Id')
def select_orders_Id(shared_data):
    orderHistoryPage = shared_data['orderHistory_page']
    orderId = shared_data['order_id']
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_page'] = orderDetailsPage
    
    
@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetails_page']
    orderDetailsPage.verifyOrderMessage()