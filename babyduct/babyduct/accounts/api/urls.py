from django.urls import path
from accounts.views import CreateCustomer

url_pattern = [
    path('/new-customer', CreateCustomer.as_view(), 'create-customer')
]