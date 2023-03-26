from accounts.models import *
from .serializers import *
from .helper import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer


# Create your views here.

# authentication views

# seller registration
@swagger_auto_schema(method='post',
                     operation_description='Registration endpoint for seller.',
                     request_body= openapi.Schema(
                                    type = openapi.TYPE_OBJECT,
                                    properties = {
                                        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                        'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING),
                                        'password2': openapi.Schema(type=openapi.TYPE_STRING),
                                        'cac_reg': openapi.Schema(type=openapi.TYPE_STRING),
                                        'product_category': openapi.Schema(type=openapi.TYPE_STRING),
                                        'location': openapi.Schema(type=openapi.TYPE_STRING)
                                    }
                        ),
                     responses={
                         200: openapi.Response('Success'),
                         201: openapi.Response('Created'),
                         401: openapi.Response('Unauthorized'),
                         404: openapi.Response('Not found')
                     })
@api_view(['POST'])
def create_seller(request):
    if request.method == 'POST':
        serializer = SellerRegistrationSerializers(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["token"] = Token.objects.get(user=account).key
            data["response"] = "Registration successful"

        else:
            data = serializer.errors

        return Response(data, status=HTTP_201_CREATED)


# buyer registration
@swagger_auto_schema(method='post',
                     operation_description='Registration endpoint for buyers.',
                     request_body= openapi.Schema(
                                    type = openapi.TYPE_OBJECT,
                                    properties = {
                                        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                        'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING),
                                        'password2': openapi.Schema(type=openapi.TYPE_STRING)
                                    }),
                     responses={
                         200: openapi.Response('Success'),
                         401: openapi.Response('Unauthorized'),
                         404: openapi.Response('Not found')
                     })
@api_view(['POST'])
def create_buyer(request):

    if request.method == 'POST':
        serializer = BuyerRegistrationSerializers(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["token"] = Token.objects.get(user=account).key
            data["response"] = "Registration successful"

        else:
            data = serializer.errors

        return Response(data, status=HTTP_201_CREATED)

# login view
@swagger_auto_schema(method='post',
                     operation_description='User login endpoint .',
                     request_body = openapi.Schema(
                        type = openapi.TYPE_OBJECT,
                        properties = {
                            "email" : openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                            "password" : openapi.Schema(type=openapi.TYPE_STRING)
                        }
                     ),
                     responses={
                         200: openapi.Response('Success'),
                         401: openapi.Response('Unauthorized'),
                         404: openapi.Response('Not found')
                     })
@api_view(['POST',])
def user_login(request):
    if request.method== "POST":
        password = request.data["password"]
        data = {}

        user = User.objects.get(email=request.data["email"])
        if user.check_password(password):
            token = Token.objects.get(user=user).key
            data["token"] = token
            data["response"] = "Login successful, User Authenticated!"
            return Response(data, HTTP_202_ACCEPTED)
        else:
            data["response"] = "Invalid Password"
            return Response(data, HTTP_400_BAD_REQUEST)

# verify email view
# reset password view

# logout view
@swagger_auto_schema(method='post',
                     operation_description='User logout endpoint',
                     responses={
                         200: openapi.Response('Success'),
                         401: openapi.Response('Unauthorized'),
                         404: openapi.Response('Not found')
                     })
@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)

# users account information view
class UserAccountInformationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersAccountInformationSerializers


# buyers payment method view
class BuyerPaymentInformationView(ModelViewSet):
    queryset = BuyerPaymentInformation.objects.all()
    serializer_class = BuyerPaymentMethodSerializers

    def list(self, request):
        return Response([])
    

    def retrieve(self, request, pk):
        user = get_object_or_404(BuyerPaymentInformation, pk=pk)
        serializer = BuyerPaymentMethodSerializers(user)
        response = {}
        for key, data in serializer.data.items():
            if key == "user" or key == "payment_method":
                response[key] = data
            else:
                response[key] = char_decrypt(KEY, data)
        return Response(response, HTTP_200_OK)
        
# buyers shippment address views
class BuyerShipmentAddressCreateView(CreateAPIView):
    serializer_class = BuyerShipmentAddressSerializers

class BuyerShipmentAddressView(RetrieveAPIView):
    serializer_class = BuyerShipmentAddressSerializers

    def get(self, request, uuid):
        buyer = get_object_or_404(BuyerShipmentAddress, user=uuid)
        serializer = BuyerShipmentAddressSerializers(buyer)
        return Response(serializer.data, 200)

class BuyerShipmentAddressUpdateView(UpdateAPIView):
    serializer_class = BuyerShipmentAddressSerializers
    queryset = BuyerShipmentAddress.objects.all()
    lookup_field = "user"

class BuyerShipmentAddressDeleteView(DestroyAPIView):
    serializer_class = BuyerShipmentAddressSerializers
    queryset = BuyerShipmentAddress.objects.all()
    lookup_field = "user"

    def perform_destroy(self, instance):
        user = get_object_or_404(User, username=instance.user)
        user.delete()


# seller's views here
class SellerProfileCreateView(CreateAPIView):
    serializer_class = SellerProfileSerializers


class SellerListAPIView(ListAPIView):
    serializer_class = SellerProfileSerializers
    queryset = SellerProfile.objects.all()


class SellerProfileView(RetrieveAPIView):
    serializer_class = SellerProfileSerializers

    def get(self, request, uuid):
        """returns seller details"""
        seller = get_object_or_404(SellerProfile, user=uuid)
        serializer = SellerProfileSerializers(seller)
        return Response(serializer.data, 200)

class SellerProfileUpdateView(UpdateAPIView):
    serializer_class = SellerProfileSerializers
    queryset = SellerProfile.objects.all()
    lookup_field = "user"

class SellerProfileDeleteView(DestroyAPIView):
    serializer_class = SellerProfileSerializers
    queryset = SellerProfile.objects.all()
    lookup_field = "user"

    def perform_destroy(self, instance):
        user = get_object_or_404(User, username=instance.user)
        user.delete()

# social auth views
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GoogleLogin(SocialLoginView): 
    adapter_class = GoogleOAuth2Adapter
    callback_url = "https://localhost:8800/callback"
    client_class = OAuth2Client