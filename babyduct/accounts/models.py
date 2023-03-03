from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    def __str__(self) -> str:
        return self.first_name + self.last_name


class ConsumerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=11)


    def __str__(self):
        return "%s" % (self.user.first_name + self.user.last_name) 

    def get_absolute_url(self):
        return "consumer/profile/{}".format(self.user.uuid)

class ProducerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cac_reg_no = models.CharField(max_length=20, default="00000000000", unique=True)
    product_category = models.CharField(max_length=9, default="unknown",choices=[("toys", "toys"), ("foods", "foods"), ("cosmetics", "cosmetics"), ("fashion", "fashion")])
    location = models.CharField(max_length=150, default="unknwown", null=False)
    contact_no = models.CharField(max_length=11)
    

    
    def __str__(self):
        return "%s" % (self.user.username) 

    def get_absolute_url(self):
        return "producer/profile/{}".format(self.user.uuid)
    

# auth token creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)