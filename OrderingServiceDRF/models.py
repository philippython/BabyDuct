from django.db import models

class Ordering_Service(models.Model):
    product_name  =  models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    price =
    status =
    