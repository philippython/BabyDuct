import random
from rest_framework import serializers
from rest_framework.response import Response
from accounts.models import ConsumerProfile, ProducerProfile, User


class ProducerRegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={ "input_type":"password"}, write_only=True)
    cac_reg = serializers.CharField()
    product_category = serializers.CharField()
    location = serializers.CharField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "password2", "cac_reg", "product_category", "location"]
        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def save(self):
        email = self.validated_data["email"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        cac = self.validated_data["cac_reg"]
        product_category = self.validated_data["product_category"]
        location = self.validated_data["location"]

        username = f"{first_name}-{last_name}-{random.randint(5643, 55573)}"
        password1 = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "email already in use by another user"})
        
        if password1 != password2:
            raise serializers.ValidationError({"error": "Password and confirm Password does not match"})
        
        user = User(username=username, email=email,first_name=first_name,last_name=last_name)
        user.set_password(password1)
        user.save()

        seller = ProducerProfile(user=user, cac_reg_no=cac, product_category=product_category, location=location)
        seller.save()

        return user
    

class ConsumerRegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={ "input_type":"password"}, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "password2"]
        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def save(self):
        email = self.validated_data["email"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]

        username = f"{first_name}-{last_name}-{random.randint(5643, 55573)}"
        password1 = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "email already in use by another user"})
        
        if password1 != password2:
            raise serializers.ValidationError({"error": "Password and confirm Password does not match"})
        
        user = User(username=username, email=email,first_name=first_name,last_name=last_name)
        user.set_password(password1)
        user.save()

        buyer = ConsumerProfile(user=user)
        buyer.save()

        return user
    
class ConsumerProfileSerializers(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = ConsumerProfile
        fields = '__all__'

class ProducerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProducerProfile
        fields = '__all__'
