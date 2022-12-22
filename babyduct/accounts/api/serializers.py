from rest_framework import serializers
from accounts.models import ConsumerProfile, ProducerProfile

class ConsumerProfileSerializers(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = ConsumerProfile
        fields = '__all__'

class ProducerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProducerProfile
        fields = '__all__'
