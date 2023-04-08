from rest_framework.decorators import api_view
from rest_framework import generics,status
from .serializer import CartSerializer,CartItemSerializer
from rest_framework.response import Response
from .models import Cart,CartItem
import requests
from .helper import *
from rest_framework.authtoken.models import Token
from rest_framework import permissions
import os
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
"""



class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        #auth_header = self.request.headers.get("Authorization").split(" ")[1]

        #auth_header = request.headers.get('Authorization').split(" ")[1]
        #if auth_header is None:
        #    return Response({"error": "No authentication credentials provided"})
        breakpoint()
        response = get_buyer_id()
        print(response)
        breakpoint()
        if response.status_code != 200:
            return Response(response.json(), response.status_code)
        buyer_id = response.json()["buyer_id"]
        breakpoint()

        slug = self.kwargs.get("slug")
        if slug is None:
            return Response({"error": "No slug provided"})
        product_url = f"http://localhost:5500/api/v1/products/{slug}"
        product_response = requests.get(product_url)        
        if product_response.status_code != 200:
            return Response(product_response.json(), product_response.status_code)
        product_data = product_response.json()

        cart = Cart.objects.filter(user_id=buyer_id).first()
        if cart is None:
            cart = Cart.objects.create(user_id=buyer_id)

        CartItem.objects.create(
            cart=cart,
            product_id=product_data["id"],
            name=product_data["name"],
            price=product_data["price"],
            quantity=1
        )

        serializer.instance = cart
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemRetrieveView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
