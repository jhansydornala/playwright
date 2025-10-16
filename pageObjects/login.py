from pageObjects.dashboard import DashboardPage

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class LoginPage:
    
    def __init__(self,page):
        self.page = page
        
        
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")
        
    def login(self,userEmail,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name ="Login").click()
        dashboard_Page = DashboardPage(self.page)
        return dashboard_Page

        
    