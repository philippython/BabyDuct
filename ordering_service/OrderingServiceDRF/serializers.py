from rest_framework import serializers
from .models import Orders

class OrderingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["product_name","address","price","date_created","price","status"]