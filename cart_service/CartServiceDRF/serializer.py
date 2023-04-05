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

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cart_items')

    class Meta:
        model = Cart
        fields = ['user_id', 'product_id', 'items', 'created_at']