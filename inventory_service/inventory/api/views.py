from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from inventory.models import Product
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializers

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        if product:
            serializer = ProductSerializers(product)
            return Response(serializer.data, 200)
        return Response({"error": "Product does not exist"}, 404)


class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers


    
                