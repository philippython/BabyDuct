from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import ConsumerProfile

# class CustomerProfileSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ConsumerProfile
#         fields = '__all__'