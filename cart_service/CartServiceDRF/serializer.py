from . models import Cart,CartItem
from rest_framework import serializers


"""
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity','price','name','cart','updated']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cartitem_set')
    class Meta:
        model = Cart
        fields = ["user_id",'product_id','quantity']
"""

from .models import Cart, CartItem
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem

        fields = ['quantity', 'price', 'name', 'cart', 'created_at', 'updated_at']

"""
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cart_items')

    class Meta:
        model = Cart
        fields = ['user_id', 'product_id', 'items', 'created_at']

import requests

class CartSerializer(serializers.ModelSerializer):
    #items = CartItemSerializer(many=True, read_only=True, source='cart_items')

    class Meta:
        model = Cart
        fields = ['user_id', 'product_id', 'created_at']
        
class CartSerializer(serializers.Serializer):
    #items = CartItemSerializer(many=True, read_only=True, source='cart_items')
    user_id = CartSerializer(source = requests.get(http://localhost:5500/api/v1/products/{slug}))

    class Meta:
        model = Cart
        fields = ['user_id', 'product_id', 'created_at']
        
"""

from rest_framework import serializers
from .models import Cart, CartItem
import requests
from .helper import *
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity', 'price', 'name', 'product']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user_id', 'items', 'created_at']

    def create(self, validated_data):
        # Get user_id and product_id from the request headers
        auth_header = self.context['request'].headers.get("Authorization")
        if auth_header is None:
            raise serializers.ValidationError({"error": "No authentication credentials provided"})
        
        response = get_buyer_id(auth_header)
        if response.status_code != 200:
            raise serializers.ValidationError(response.json())

        user_id = response.json()["buyer_id"]
        slug = self.context['view'].kwargs.get("slug")
        if slug is None:
            raise serializers.ValidationError({"error": "No slug provided"})
        product_url = f"http://localhost:5000/api/v1/products/{slug}"
        product_response = requests.get(product_url)        
        if product_response.status_code != 200:
            raise serializers.ValidationError(product_response.json())

        product_data = product_response.json()
        product_id = product_data["id"]
        
        # Save the cart with user_id and product_id as default values
        cart = Cart.objects.create(user_id=user_id, product_id=product_id)
        
        # Create or update the cart item with the foreign key and quantity
        cart_item, created = CartItem.objects.update_or_create(
            cart=cart, product=product_id, defaults={'quantity': 1, 'price': product_data["price"], 'name': product_data["name"]}
        )
        
        validated_data['user_id'] = user_id
        validated_data['items'] = [cart_item]
        return super().create(validated_data)
