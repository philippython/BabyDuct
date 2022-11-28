from accounts.api.serializers import CustomerProfileSerializers, CreateUserSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer

  
            
class CreateCustomerProfileView(CreateAPIView):
    serializer_class = CustomerProfileSerializers