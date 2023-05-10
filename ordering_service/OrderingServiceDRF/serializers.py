from rest_framework import serializers
from .models import Orders

class OrderingServiceSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(read_only=True)
    price = serializers.DecimalField(read_only=True,max_digits=8,decimal_places=2)
    product_name = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    street = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    cart_id = serializers.CharField(read_only=True)
    


    class Meta:
        model = Orders
        fields = "__all__"