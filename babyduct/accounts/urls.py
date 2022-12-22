from django.urls import path
from accounts.views import *


app_name = 'accounts'
urlpatterns = [
    # consumer urls
    path('consumer/create-profile', ConsumerProfileCreateView.as_view(), name='create_consumer_profile'),
    path('consumer/all', ConsumerListAPIView.as_view(), name='all_consumers'),
    path('consumer/profile/<str:uuid>', ConsumerProfileView.as_view(), name='consumer_pofile'),
    path('consumer/profile/<str:user>/edit', ConsumerProfileUpdateView.as_view(), name='edit_consumer_pofile'),
    path('consumer/profile/<str:user>/delete', ConsumerProfileDeleteView.as_view(), name='delete_consumer_profile')

]