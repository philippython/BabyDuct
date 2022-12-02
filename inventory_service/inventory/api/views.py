from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from inventory.models import Product, ProductsImage
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers


    
                