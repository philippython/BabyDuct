import requests

#URL = "https://babyduct-inventory-service.onrender.com/api/v1/accounts/auth/obtain-buyer-id"
URL = "http://localhost:5000/api/v1/accounts/auth/obtain-buyer-id"
#def get_buyer_id(header):
#    """ function to return authentication token or or custom error message"""
#    auth_token = header.split(" ")[1]
#    if auth_token:
#        headers = {
#            "Authorization": f"Token {auth_token}"
#        }
#        return requests.get(URL, headers=headers)
    
def get_buyer_id():
    """ function to return authentication token or or custom error message"""
    
    return requests.get(URL)
print(get_buyer_id())
    
        