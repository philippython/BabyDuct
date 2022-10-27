from django.urls import path
from accounts.views import CreateCustomerProfileView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), 'register'),
    path('new-customer-profile', CreateCustomerProfileView.as_view(), 'create_customer_profile')
]