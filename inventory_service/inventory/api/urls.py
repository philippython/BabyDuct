from django.urls import path
from .views import ProductCreateView, ProductDetailView,  ReviewCreateView, ProductListView

urlpatterns = [
    path("product/<slug:slug>", ProductDetailView.as_view(), name="single-product"),
    path("all-products", ProductListView.as_view(), name="all_products"),
    path("new-product", ProductCreateView.as_view(), name="create_product"),
    path("new-review", ReviewCreateView.as_view(), name="review_product"),
]