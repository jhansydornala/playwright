from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961719320a140fe1ca57c"}]}



class APIUtils:
    
    def getToken(self,playwright:Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                 data={"userEmail": "jhansy@yopmail.com", "userPassword": "Abc@12345"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]
         
    
    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"
                                          })
        print(response.json())
        print(response)
        print(response.text)
        response_body = response.json()
        orderId = response_body["orders"][0]
        print(response_body)
        print(orderId)
        return orderId        
    