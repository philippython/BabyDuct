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
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ["id", "name", "description", "category", "price", "date", "images", "reviews", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        
        for image in uploaded_images:
            ProductsImage.objects.create(product=product, image=image)

        return product