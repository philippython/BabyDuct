from ast import Mod
from rest_framework import serializers
from inventory.models import Product, Review

class ProductSerializers(serializers.ModelSerializers):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    images = serializers.ListField(child=serializers.ImageField(upload_to="products"))

    class Meta:
        model = Product
        fields = ["name","description", "category", "price", "date"]

class ReviewSerializers(serializers.ModelSerializers):
    class Meta:
        model = Review 
        fields = "__all__"
