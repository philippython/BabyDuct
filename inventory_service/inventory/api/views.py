from rest_framework.generics import APIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from inventory.models import Product, ProductsImage
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers

class ProductsImageCreateView(APIView):

    def get(self, request):
        images = ProductsImage.objects.all()
        serializer = ProductsImageSerializers(images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
    