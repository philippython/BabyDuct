from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,status
from .serializer import CartSerializer,CartItemSerializer
from rest_framework.response import Response
from .models import Cart,CartItem
import requests


from rest_framework.authtoken.models import Token

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
# Using custom user model
def get_token(request):
    # Get the user's token
    token = Token.objects.get(user=request.user)
    return token
    #print(token)

    # Use the token to authenticate with the external service
    #headers = {
        #'Authorization': f'Token {token.key}'
    #}
    # Get the user's UUID
    #user_uuid = request.user.uuid
    #print(user_uuid)

    # Build the URL with the user's UUID
    #url = f"https://babyduct-accounts-service.onrender.com/account-information/{user_uuid}"
    #response = requests.get(url, headers=headers)

    #if response.status_code != 200:
    #    return "User not found"
    # return response.json()
class AddToCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        slug = kwargs['slug']
        header = {'Authorization': f'Token {get_token()}'}
        response = requests.get(f"https://babyduct-inventory-service.onrender.com/products/{slug}", headers=header)

        if response.status_code != 200:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product_data = response.json()

        cart, _ = Cart.objects.get_or_create(user_id=user_id)
        cart_item, created = CartItem.objects.get_or_create(name=product_data['name'], price=product_data['price'], cart=cart)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
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

