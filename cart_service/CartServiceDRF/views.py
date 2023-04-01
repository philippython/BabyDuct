from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,status
from .serializer import CartSerializer,CartItemSerializer
from rest_framework.response import Response
from .models import Cart,CartItem
import requests

"""
("https://babyduct-accounts-service.onrender.com/account-information{uuid}")
#username=chidera
#lastname = onumajuru
#password chidera11
#dicta@gmail.com
{
  "token": "e5500c909baa3bac05365a76c6972f56bfa23c98",
  "response": "Registration successful"
}
{
  "token": "e5500c909baa3bac05365a76c6972f56bfa23c98",
  "response": "Login successful, User Authenticated!"
}
{
  "token": "3c85dca25ce94e659458cfed161cee369e940984",
  "response": "Login successful, User Authenticated!"
}
"""

import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart
data = {
    'username':input(),
    'password':input()
}
def get_token():
    url = "https://babyduct-accounts-service.onrender.com/account-information{uuid}"
    response = requests.post(url,data=data)
    if response.status_code != 200:
        return("User not found")
    return response.json()

  
@api_view(['POST'])
def add_to_cart(request, slug):
    user_id = request.user.id 
    header = {'Authorization':f'Token{get_token()}'}
    response = requests.get(f"https://babyduct-inventory-service.onrender.com/products/{slug}",headers=header)
    if response.status_code != 200:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    product_data = response.json()

    product, created = CartItem.objects.get_or_create(name=product_data['name'], price=product_data['price'])
    if not created:
        product.quantity += 1
        product.save()
    cart = Cart.objects.create(user_id=user_id)
    cart_item = CartItem.objects.create(cart=cart, **product_data)
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartItemDeleteView(generics.DestroyAPIView):
    cart = CartItem.objects.all()
    queryset = CartItemSerializer

class CartItemUpdateView(generics.UpdateAPIView):
    cart = CartItem.objects.all()
    queryset = CartItemSerializer

class CartItemRetrieveView(generics.RetrieveAPIView):
    cart = CartItem.objects.all()
    queryset = CartItemSerializer