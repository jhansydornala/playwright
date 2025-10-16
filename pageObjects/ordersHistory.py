from pageObjects.orderDetails import OrderDetailsPage

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class OrderHistoryPage:
    
    def __init__(self,page):
        self.page = page
        
        
    def selectOrder(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role("button", name="View").click(timeout=6000)
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage