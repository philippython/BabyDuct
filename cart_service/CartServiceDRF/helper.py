import requests

URL = "https://babyduct-accounts-service.onrender.com/api/v1/accounts/auth/obtain-buyer-id"
def get_buyer_id(header):
    """ function to return authentication token or or custom error message"""
    auth_token = header.split(" ")[1]
    if auth_token:
        headers = {
            "Authorization": f"Token {auth_token}"
        }
        return requests.get(URL, headers=headers)
    

def get_products_data(slug):
    if slug == None:
        return "slug is required"
    else:
        return requests.get("https://babyduct-inventory-service.onrender.com/api/v1/inventory/products/{slug}")


