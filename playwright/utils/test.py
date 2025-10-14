import requests

def get_token():
    url = "https://rahulshettyacademy.com/api/ecom/auth/login"
    resp = requests.post(url, json={"userEmail": "jhansy@yopmail.com", "userPassword": "Abc@12345"})
    resp.raise_for_status()                # raise if login failed (HTTP error)
    data = resp.json()
    print("Login headers:", resp.headers)
    # debug:
    print("login response:", data)
    token = data.get("token")
    if not token:
        raise RuntimeError("No token in login response")
    return token

token = get_token()
print("token:", token)

url = "https://rahulshettyacademy.com/api/ecom/order/create-order"
orders_payload = {"orders": [{"country": "India", "productOrderedId": "68a961719320a140fe1ca57c"}]}

headers = {
    "Authorization": f"{token}",        # include Bearer prefix
    "Content-Type": "application/json"         # correct content type
}

# send JSON body using `json=` so requests handles serialization and headers
resp = requests.post(url, json=orders_payload, headers=headers)

print("status:", resp.status_code)
try:
    print("response json:", resp.json())
except ValueError:
    print("response text:", resp.text)
