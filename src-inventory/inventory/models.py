from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(models.Model):
    seller = models.CharField(max_length=255, default="product_owner")
    seller_id = models.UUIDField()
    name = models.CharField(max_length=50, unique=True, blank=False)
    description = models.CharField(max_length=255, blank=False)
    slug = models.CharField(max_length=80, blank=False, null=False)
    category = models.CharField(max_length=9, choices=[("toys", "toys"), ("foods", "foods"), ("cosmetics", "cosmetics"), ("fashion", "fashion")])
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'slug' : self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name)

class Review(models.Model):
    reviewer_id = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    slug = models.CharField(max_length=80, blank=False, null=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(max_length=255)
    date = models.DateField(auto_now=True)


    def get_absoute_url(self):
        return  "/inventory/product/reviews/%s" % (self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.review)

class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="products")

    
    def __str__(self):
        return "%s" % (self.product.name)