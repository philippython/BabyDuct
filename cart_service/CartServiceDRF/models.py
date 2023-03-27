from django.db import models
import requests

class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField() 
    date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField()