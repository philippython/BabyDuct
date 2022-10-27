from accounts.api.serializers import CustomerProfileSerializers, CreateUserSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer

    # def get_queryset(self, request):
    #     if request.method == 'POST':
    #         user = User.object.get(username=request.username)
    #         if user :
    #             return ValidationError("User already exists", 400)
    #         return []
            
class CreateCustomerProfileView(CreateAPIView):
    serializer_class = CustomerProfileSerializers