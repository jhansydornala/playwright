import json
import os
from playwright.sync_api import Playwright, expect
import pytest

from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage
from utils.api_Base import APIUtils

#Json file -> util -> access into test 

with open('data/credentials.json') as f :
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']
    
@pytest.mark.parametrize('user_credentials', user_credential_list)
def test_web_api(playwright: Playwright, user_credentials):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']
    firefoxbrowser = playwright.firefox.launch(headless=False)
    context = firefoxbrowser.new_context()
    page = context.new_page()      
#creatorder-OrderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)    
#login
    login_Page = LoginPage(page)#object for login page class
    login_Page.navigate()
    dashboard_Page = login_Page.login(username, password)
#dashboardPage
    orderHistoryPage = dashboard_Page.selectOrdersNavLink()
    orderHistoryPage = orderHistoryPage.selectOrder(orderId)
    orderHistoryPage.verifyOrderMessage()
    context.close()