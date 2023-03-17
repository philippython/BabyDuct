from django.shortcuts import render
import requests
from rest_framework import generics
from .models import Ordering_Service
from .serializers import OrderingServiceSerializer


class OrderingServiceCreateView(generics.CreateAPIView):
    queryset = Ordering_Service.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceSingleView(generics.RetrieveAPIView):
    queryset = Ordering_Service.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceUpdateView(generics.UpdateAPIView):
    queryset = Ordering_Service.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceDeleteView(generics.DestroyAPIView):
    queryset = Ordering_Service.objects.all()
    serializer_class = OrderingServiceSerializer


class OrderingServiceListView(generics.ListAPIView):
    queryset = Ordering_Service.objects.all()
    serializer_class = OrderingServiceSerializer

