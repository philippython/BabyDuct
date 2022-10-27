from rest_framework import serializers
from accounts.models import Customer_Profile

class CustomerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Profile
        fields = '__all__'