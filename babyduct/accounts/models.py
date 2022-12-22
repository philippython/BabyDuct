from distutils.command.upload import upload
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
    profile_image  =  models.ImageField(null=True, max_length=100, upload_to='consumers')
    contact_no = models.CharField(max_length=11)
    age = models.IntegerField()


    def __str__(self):
        return "%s" % (self.user.username) 

class ProducerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, null=False)
    company_logo  =  models.ImageField(null=True, max_length=100, upload_to='producers', unique=True)
    company_email = models.EmailField()
    contact_no = models.CharField(max_length=11)

    
    def __str__(self):
        return "%s" % (self.user.username) 
