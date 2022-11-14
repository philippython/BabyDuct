from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image  =  models.ImageField(null=True)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    contact_no = models.CharField(max_length=11)

    