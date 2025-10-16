from playwright.sync_api import expect

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class OrderDetailsPage:
    
    def __init__(self,page):
        self.page = page
        
        
    def verifyOrderMessage(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")