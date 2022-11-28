from math import prod
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from inventory.models import Product
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers

class ProductsImageCreateView(CreateAPIView):
    serializer_class = ProductsImageSerializers
