from accounts.api.serializers import ConsumerProfileSerializers, ProducerProfileSerializers
from rest_framework.generics import CreateAPIView


# Create your views here.

class ConsumerProfileCreateView(CreateAPIView):
    serializer_class = ConsumerProfileSerializers

