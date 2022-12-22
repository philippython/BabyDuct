from accounts.api.serializers import ConsumerProfileSerializers, ProducerProfileSerializers
from accounts.models import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response


# Create your views here.

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
