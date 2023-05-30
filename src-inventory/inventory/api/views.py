from .helper import *
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView , UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from inventory.models import Product, Review
from django_filters.rest_framework import DjangoFilterBackend
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers

class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        auth_header = self.request.headers.get("Authorization")
        if auth_header != None:
            response = get_seller_data(auth_header)
            if response.status_code == 200 : 
                uuid = response.json()["seller_id"]
                seller = response.json()["seller_name"]
                serializer.save(seller_id=uuid, seller=seller)
            else : 
                return Response(response.json(), response.status_code)
        else:
            return Response({"error": "No authentication credentials provided"})
        
class ProductListView(ListAPIView):
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller']
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializers

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializers(product)
        return Response(serializer.data, 200)

class ProductUpdateView(UpdateAPIView):
    parser_class = [MultiPartParser, FormParser]
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializers

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "slug"

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers

class ReviewsListView(ListAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    lookup_field = "slug"

class ReviewUpdateView(UpdateAPIView):
    queryset = Review.objects.all()
    lookup_field = "slug"
    serializer_class = ReviewSerializers

class ReviewDeleteView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = "slug"


class UserReviewsListView(ListAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    lookup_field = "date"