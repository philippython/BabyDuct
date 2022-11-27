from pyexpat import model
from unicodedata import category
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=9, choices=[("toys", "toys"), ("foods", "foods"), ("cosmetics", "cosmetics"), ("fashion", "fashion")])
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "%s" % (self.name)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinLengthValidator(0), MaxValueValidator(5)])
    review = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.review)