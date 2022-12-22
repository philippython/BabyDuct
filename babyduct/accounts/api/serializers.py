from rest_framework import serializers
from accounts.models import ConsumerProfile, ProducerProfile

class ConsumerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConsumerProfile
        fields = '__all__'

class ProducerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProducerProfile
        fields = '__all__'
