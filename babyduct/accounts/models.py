from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField()

    def __str__(self) -> str:
        return self.username

class UserProfile(models.Model):

    bio = models.TextField(null=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image  =  models.ImageField(null=True, max_length=100, upload_to='consumer')
    contact_no = models.CharField(max_length=11)
    is_producer = models.BooleanField(default=False)
    age = models.IntegerField()



    def __str__(self):
        return "%s" % (self.user) 

    