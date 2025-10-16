from pageObjects.ordersHistory import OrderHistoryPage

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class DashboardPage:
    
    
    def __init__(self,page):
        self.page = page
        
        
    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name ="ORDERS").click() 
        orderHistoryPage = OrderHistoryPage(self.page)  
        return orderHistoryPage