from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Customer_Profile


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password" : {"write_only": True}
        }


class CustomerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Profile
        fields = '__all__'