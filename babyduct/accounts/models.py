from django.db import models
from uuid import uuid4
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    def __str__(self) -> str:
        return self.first_name + self.last_name

class BuyerPaymentInformation(models.Model):
    def validate_expiry_date(value):
        if value.count("/") != 1 or len(value) > 7:
            raise ValidationError({"Invalid expiry date"}, 400)
        if value.index("/") != 2 : 
            raise ValidationError({"Invalid expiry date"}, 400)


        
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    card_name = models.CharField(max_length=55, null=False)
    card_number = models.CharField(max_length=16,validators=[MinLengthValidator(11)], null=False)
    cvv = models.CharField(max_length=3, null=False)
    payment_method = models.CharField(max_length=55)
    expiry_date = models.CharField(max_length=7, null=False, validators=[validate_expiry_date])

    def __str__(self) -> str:
        return self.user.first_name + self.user.last_name
        
class BuyerShipmentAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=11,  validators=[MinLengthValidator(11)])
    phone_no_2 = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=True)
    country = models.CharField(max_length=55, null=False)
    state = models.CharField(max_length=55, null=False)
    city = models.CharField(max_length=55, null=False)
    street = models.CharField(max_length=55, null=False)


    def __str__(self):
        return "%s" % (self.user.first_name + self.user.last_name) 

    def get_absolute_url(self):
        return "buyer/shipment/{}".format(self.user.uuid)

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cac_reg_no = models.CharField(max_length=20, unique=True)
    product_category = models.CharField(max_length=9,choices=[("toys", "toys"), ("foods", "foods"), ("cosmetics", "cosmetics"), ("fashion", "fashion")])
    location = models.CharField(max_length=150, null=False)
    contact_no = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    

    
    def __str__(self):
        return "%s" % (self.user.username) 

    def get_absolute_url(self):
        return "seller/profile/{}".format(self.user.uuid)
    

# auth token creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)