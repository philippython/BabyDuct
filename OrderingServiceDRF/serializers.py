from rest_framework import serializers
from .models import Ordering_Service

class OrderingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering_Service
        fields = ("product_name","address","price","date_created","price","status")