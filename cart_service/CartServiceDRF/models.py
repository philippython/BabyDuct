from django.db import models
import requests
"""
class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField() 
    created_at = models.DateField(auto_now=True)
    

class CartItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)

"""

from django.db import models

class Cart(models.Model):
    user_id = models.UUIDField(max_length=500)
    product_id = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"Cart {self.pk} (User {self.user_id}, Product {self.product_id})"

class CartItem(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="items")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def _str_(self):
        return f"CartItem {self.pk} ({self.name})"