from . models import Cart,CartItem
from rest_framework import serializers
from .helper import *

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','quantity', 'price', 'name','cart']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True,many=True,source='items.all')
    user_id = serializers.UUIDField(read_only=True)
    product_id = serializers.CharField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id','user_id','product_id', 'created_at','items']
     
        

    