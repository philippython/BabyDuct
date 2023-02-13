from django.urls import path
from .views import *
from django import utils


urlpatterns = [
    # consumer urls
    path('consumer/create-profile', ConsumerProfileCreateView.as_view(), name='create_consumer_profile'),
    path('consumer/all', ConsumerListAPIView.as_view(), name='all_consumers'),
    path('consumer/profile/<str:uuid>', ConsumerProfileView.as_view(), name='consumer_pofile'),
    path('consumer/profile/<str:user>/edit', ConsumerProfileUpdateView.as_view(), name='edit_consumer_pofile'),
    path('consumer/profile/<str:user>/delete', ConsumerProfileDeleteView.as_view(), name='delete_consumer_profile'),


    # producer urls
    path('producer/create-profile', ProducerProfileCreateView.as_view(), name='create_producer_profile'),
    path('producer/all', ProducerListAPIView.as_view(), name='all_producers'),
    path('producer/profile/<str:uuid>', ProducerProfileView.as_view(), name='producer_pofile'),
    path('producer/profile/<str:user>/edit', ProducerProfileUpdateView.as_view(), name='edit_producer_pofile'),
    path('producer/profile/<str:user>/delete', ProducerProfileDeleteView.as_view(), name='delete_producer_profile')
]