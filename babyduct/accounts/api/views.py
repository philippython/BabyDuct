from accounts.models import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from .serializers import ( ConsumerProfileSerializers, ProducerProfileSerializers,
                           ProducerRegistrationSerializers, ConsumerRegistrationSerializers )


# Create your views here.

# authentication views

# producer registration
@api_view(['POST'])
def create_producer(request):

    if request.method == 'POST':
        serializer = ProducerRegistrationSerializers(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["token"] = Token.objects.get(user=account).key
            data["response"] = "Registration successful"

        else:
            data = serializer.errors

        return Response(data, status=HTTP_201_CREATED)


# consumer registration
@api_view(['POST'])
def create_consumer(request):

    if request.method == 'POST':
        serializer = ConsumerRegistrationSerializers(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["token"] = Token.objects.get(user=account).key
            data["response"] = "Registration successful"

        else:
            data = serializer.errors

        return Response(data, status=HTTP_201_CREATED)

# login view
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

# logout view
@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)
# password reset view

# application views
class ConsumerProfileCreateView(CreateAPIView):
    serializer_class = ConsumerProfileSerializers


class ConsumerListAPIView(ListAPIView):
    serializer_class = ConsumerProfileSerializers
    queryset = ConsumerProfile.objects.all()


class ConsumerProfileView(RetrieveAPIView):
    serializer_class = ConsumerProfileSerializers

    def get(self, request, uuid):
        consumer = get_object_or_404(ConsumerProfile, user=uuid)
        serializer = ConsumerProfileSerializers(consumer)
        return Response(serializer.data, 200)

class ConsumerProfileUpdateView(UpdateAPIView):
    serializer_class = ConsumerProfileSerializers
    queryset = ConsumerProfile.objects.all()
    lookup_field = "user"

class ConsumerProfileDeleteView(DestroyAPIView):
    serializer_class = ConsumerProfileSerializers
    queryset = ConsumerProfile.objects.all()
    lookup_field = "user"

    def perform_destroy(self, instance):
        user = get_object_or_404(User, username=instance.user)
        user.delete()


# producer views here
class ProducerProfileCreateView(CreateAPIView):
    serializer_class = ProducerProfileSerializers


class ProducerListAPIView(ListAPIView):
    serializer_class = ProducerProfileSerializers
    queryset = ProducerProfile.objects.all()


class ProducerProfileView(RetrieveAPIView):
    serializer_class = ProducerProfileSerializers

    def get(self, request, uuid):
        Producer = get_object_or_404(ProducerProfile, user=uuid)
        serializer = ProducerProfileSerializers(Producer)
        return Response(serializer.data, 200)

class ProducerProfileUpdateView(UpdateAPIView):
    serializer_class = ProducerProfileSerializers
    queryset = ProducerProfile.objects.all()
    lookup_field = "user"

class ProducerProfileDeleteView(DestroyAPIView):
    serializer_class = ProducerProfileSerializers
    queryset = ProducerProfile.objects.all()
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