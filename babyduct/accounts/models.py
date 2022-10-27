from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer_Profile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField()
    age = models.IntegerField()
    contact_no = models.CharField()

    