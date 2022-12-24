from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self) -> str:
        return self.username


class ConsumerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=150, null=False)
    profile_image = models.ImageField(null=True, max_length=100, upload_to='consumers')
    contact_no = models.CharField(max_length=11)


    def __str__(self):
        return "%s" % (self.user.username) 

    def get_absolute_url(self):
        return "consumer/profile/{}".format(self.user.uuid)

class ProducerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=150, null=False)
    store_logo = models.ImageField(null=True, max_length=100, upload_to='producers', unique=True)
    store_email = models.EmailField()
    location = models.CharField(max_length=150, null=False)
    business_certificate = models.FileField(upload_to='Files')
    contact_no = models.CharField(max_length=11)

    
    def __str__(self):
        return "%s" % (self.user.username) 

    def get_absolute_url(self):
        return "producer/profile/{}".format(self.user.uuid)