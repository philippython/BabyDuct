from accounts.api.serializers import ConsumerProfileSerializers, ProducerProfileSerializers
from accounts.models import ConsumerProfile, ProducerProfile
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response


# Create your views here.

class ConsumerProfileCreateView(CreateAPIView):
    serializer_class = ConsumerProfileSerializers

class ConsumerProfileView(RetrieveAPIView):
    serializer_class = ConsumerProfileSerializers

    def get(self, request, uuid):
        consumer = get_object_or_404(ConsumerProfile, uuid=uuid)
        serializer = ConsumerProfileSerializers(consumer)
        return Response(serializer.data, 200)

class ConsumerListAPIView(ListAPIView):
    serializer_class = ConsumerProfileSerializers
    queryset = ConsumerProfile.objects.all()
    