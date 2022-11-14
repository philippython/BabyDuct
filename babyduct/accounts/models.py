from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer_Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image  =  models.ImageField(null=True, max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    contact_no = models.CharField(max_length=11)


    def __str__(self):
        return "%s" % (self.user) 

    