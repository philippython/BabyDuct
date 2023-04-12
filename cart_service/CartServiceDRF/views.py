from rest_framework.decorators import api_view
from rest_framework import generics,status
from .serializer import CartSerializer,CartItemSerializer
from rest_framework.response import Response
from .models import Cart,CartItem
import requests
from .helper import *

"""
buyer {
  "first_name": "chi",
  "last_name": "onu",
  "email": "osinachi1@example.com",
  "password": "chidera111",
  "password2": "chidera111"
  {
  "token": "3ab92c9d217887f9237bbca60b5afcd0fe1087d6",
  "response": "Registration successful"
}
}
"""

"""

[{"id":1,"seller_id":"613cb4ff-c570-40bc-be9f-d9b4cee82c5f","seller":"osionu",
"name":"test product 2",
"url":"/api/v1/inventory/products/test-product-2",
"description":"test product
seller {
  "first_name": "ste",
  "last_name": "onu",
  "email": "stella@example.com",
  "password": "chidera111",
  "password2": "chidera111",
  "cac_reg": "4455333",
  "product_category": "Toys",
  "location": "Nigeria"
}
{
  "token": "4287ecf1aff873972cad313afc2f5d149e8de070",
  "response": "Registration successful"
}
product_data = {"name": "Product 1", "price": 9.99, "description": "A great product"}
serializer = CartSerializer(data={**validated_data, **product_data})
if serializer.is_valid():
    serializer.save(buyer_id=buyer_id)

"""



class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    def perform_create(self,serializer):
        auth_header = self.request.headers.get("Authorization")       
        response = get_buyer_id(auth_header)      
        buyer_id = response.json()["buyer_id"]
        slug = self.request.headers.get("slug")
        product_response = requests.get(f"https://babyduct-inventory-service.onrender.com/api/v1/inventory/products/{slug}")
        product_data = product_response.json()
        product_id = product_data["id"]
        product_price = product_data["price"]
        product_name = product_data["name"]
        cart = serializer.save(user_id=buyer_id,product_id=product_id)
        cart_items_data = [{"price": product_price, "name": product_name, "cart": cart.id}]
        cart_item_serializer = CartItemSerializer(data=cart_items_data, many=True)
        cart_item_serializer.is_valid(raise_exception=True)
        cart_item_serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response("Cart item deleted sucessfully",status=status.HTTP_200_OK) 

class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemListView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemRetrieveView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
