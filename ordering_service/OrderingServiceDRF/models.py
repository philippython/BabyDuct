from django.db import models
ORDER_STATUS =  {
    ("1","pending"),
    ("2","completed"),
    ("3","cancelled")

}
class Orders(models.Model):
    user_id = models.IntegerField()
    order_id = models.Field(primary_key=True)
    product_name  =  models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    status = models.CharField(max_length=50,Choices = ORDER_STATUS,default ='1')    

    def __str__(self):
        return self.product_name
    
    