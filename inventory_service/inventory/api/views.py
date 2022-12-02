from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from inventory.models import Product, ProductsImage
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers


    
                