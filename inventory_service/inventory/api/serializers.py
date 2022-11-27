from rest_framework import serializers
from inventory.models import Product, Review

class ProductSerializers(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False, use_url="products"))

    class Meta:
        model = Product
        fields = ["name","description", "category", "price", "date", "images", "reviews"]

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = "__all__"
