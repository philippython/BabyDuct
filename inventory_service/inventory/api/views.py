from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView , UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from inventory.models import Product
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

class ProductListView(ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializers

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializers(product)
        return Response(serializer.data, 200)

class ProductUpdateView(UpdateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers


    
                