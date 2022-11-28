from rest_framework import serializers
from inventory.models import Product, Review, ProductsImage


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review 
        exclude = ["slug"]


class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True, read_only=True)
    images =  ProductsImageSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ["slug"]
