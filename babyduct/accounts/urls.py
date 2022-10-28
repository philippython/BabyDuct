from django.urls import path
from accounts.views import CreateCustomerProfileView, RegisterView


app_name = 'accounts'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register_user'),
    path('new-customer-profile', CreateCustomerProfileView.as_view(), name='create_customer_profile')
]