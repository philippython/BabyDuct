from api.serializers import CustomerProfileSerializers
from rest_framework.generics import CreateAPIView

# Create your views here.
class CreateCustomer(CreateAPIView):
    serializer_class = CustomerProfileSerializers