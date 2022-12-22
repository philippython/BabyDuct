from django.urls import path
from accounts.views import ConsumerProfileCreateView


app_name = 'accounts'
urlpatterns = [
    # consumer urls
    path('consumer/create-profile', ConsumerProfileCreateView.as_view(), name='create_customer_profile')
]