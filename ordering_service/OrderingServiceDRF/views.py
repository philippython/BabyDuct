from django.shortcuts import render
from rest_framework import generics,status
from .models import Orders
import requests
from .serializers import OrderingServiceSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from .helper import *


class OrderingServiceCreateView(generics.CreateAPIView):
    serializer_class = OrderingServiceSerializer

    def perform_create(self, serializer):  
        auth_header = self.request.headers.get("Authorization")   
        response = get_buyer_id(auth_header)
        buyer_id = response.json()["buyer_id"]
        id = self.request.headers.get("id")
        cart_response = requests.get(f"https://babyduct-cart-service.onrender.com/api/v1/cart-item/{id}/retrieve")
        cart = cart_response.json()
        print(cart)
        cart_id = cart["id"]
        product_name = cart["name"]
        product_price = cart["price"]
        uuid = self.request.headers.get("uuid")
        print(uuid)
        shipping_information_response = requests.get(f"https://babyduct-accounts-service.onrender.com/api/v1/accounts/buyer/shipment/{uuid}")
        print(shipping_information_response)
        shipping_information  = shipping_information_response.json()
        cart = serializer.save(user_id=buyer_id,cart_id=cart_id,product_name=product_name,price=product_price,country=shipping_information["country"],state=shipping_information["state"],city=shipping_information["city"],street=shipping_information["street"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
class OrderingServiceSingleView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data['status'] in ['completed', 'cancelled']:
            instance.status = request.data['status']
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"status": "Invalid status value. Valid values are 'completed' or 'cancelled'."})

class OrderingServiceDeleteView(generics.DestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer
    
    

class OrderingServiceListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

