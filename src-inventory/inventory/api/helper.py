import requests

URL = "https://babyduct-inventory-service.onrender.com/api/v1/accounts/auth/obtain-seller-data"

def get_seller_data(header):
    """ function to return authentication token or or custom error message"""
    auth_token = header.split(" ")[1]
    if auth_token:
        headers = {
            "Authorization": f"Token {auth_token}"
        }
        return requests.get(URL, headers=headers)
        