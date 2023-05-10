from django.db import models
from uuid import uuid4

ORDER_STATUS =  {
    ("pending","Pending"),
    ("completed","Completed"),
    ("cancelled","Cancelled")

}
class Orders(models.Model):
    user_id = models.UUIDField()
    order_id = models.AutoField(primary_key=True)
    cart_id = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    status = models.CharField(max_length=50,choices=ORDER_STATUS,default ='1') 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.product_name
    
class OrderReceipt(models.Model):
    order = models.ForeignKey(Orders,related_name="order_item",on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    