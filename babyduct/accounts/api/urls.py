from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("account-information", UserAccountInformationView)
router.register("payment-information", BuyerPaymentInformationView)

urlpatterns = [

    # auth urls
    path('auth/register/seller', create_seller, name='register_seller'),
    path('auth/register/buyer', create_buyer, name='register_buyer'),
    path('auth/obtain-seller-data', obtain_seller_data, name='obtain_seller_data'),
    path('auth/obtain-buyer-id', obtain_buyer_id, name='obtain_buyer_id'),
    path('auth/login', user_login, name="user_login"),
    path('auth/logout', logout_view, name="logout" ),


    # buyer shipment address endpoint
    path('buyer/create-shipment', BuyerShipmentAddressCreateView.as_view(), name='create_buyer_shipment'),
    path('buyer/shipment/<str:uuid>', BuyerShipmentAddressView.as_view(), name='buyer_shipment'),
    path('buyer/shipment/<str:user>/edit', BuyerShipmentAddressUpdateView.as_view(), name='edit_buyer_shipment'),
    path('buyer/shipment/<str:user>/delete', BuyerShipmentAddressDeleteView.as_view(), name='delete_buyer_shipment'),

    # seller urls
    path('seller/create-profile', SellerProfileCreateView.as_view(), name='create_seller_profile'),
    path('seller/all', SellerListAPIView.as_view(), name='all_sellers'),
    path('seller/profile/<str:uuid>', SellerProfileView.as_view(), name='seller_pofile'),
    path('seller/profile/<str:user>/edit', SellerProfileUpdateView.as_view(), name='edit_seller_pofile'),
    path('seller/profile/<str:user>/delete', SellerProfileDeleteView.as_view(), name='delete_seller_profile')
] 

urlpatterns += router.urls