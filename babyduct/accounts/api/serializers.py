import random
from .helper import *
from accounts.models import *
from rest_framework import serializers

class SellerRegistrationSerializers(serializers.ModelSerializer):
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

        seller = SellerProfile(user=user, cac_reg_no=cac, product_category=product_category, location=location)
        seller.save()

        return user
    

class BuyerRegistrationSerializers(serializers.ModelSerializer):
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

        buyer = BuyerShipmentAddress(user=user)
        buyer.save()

        return user
    
class UsersAccountInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class BuyerPaymentMethodSerializers(serializers.ModelSerializer):
    class Meta:
        model = BuyerPaymentInformation
        fields = ["user", "card_name", "card_number", "payment_method", "cvv", "expiry_date"]
    
    def save(self):
        user = self.validated_data["user"]
        payment_method = self.validated_data["payment_method"]
        card_name = char_encrypt(KEY, str(self.validated_data["card_name"]).lower())
        card_number = char_encrypt(KEY,str(self.validated_data["card_number"]).lower())
        cvv = char_encrypt(KEY, str(self.validated_data["cvv"]))
        expiry_date = char_encrypt(KEY, str(self.validated_data["expiry_date"]))

        info = BuyerPaymentInformation(user=user, card_name=card_name, card_number=card_number, 
                                       cvv=cvv, expiry_date=expiry_date, payment_method=payment_method)
        info.save()

        return info


class BuyerShipmentAddressSerializers(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = BuyerShipmentAddress
        fields = '__all__'

class SellerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = '__all__'
