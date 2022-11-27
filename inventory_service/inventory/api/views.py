from math import prod
from rest_framework.generics import CreateAPIView
from inventory.api.serializers import ProductSerializers, ReviewSerializers

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers
