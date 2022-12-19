from django.urls import path
from .views import  *

urlpatterns = [

    # products endpoints
    path("product/<slug:slug>", ProductDetailView.as_view(), name="single-product"),
    path("product/<slug:slug>/edit", ProductUpdateView.as_view(), name="edit_product"),
    path("product/<slug:slug>/delete", ProductDeleteView.as_view(), name="delete_product"),
    path("product/new-product", ProductCreateView.as_view(), name="create_product"),
    path("all-products", ProductListView.as_view(), name="all_products"),
    
    # reviews endpoints
    path("product/reviews/review-create", ReviewCreateView.as_view(), name="review_product"),
    path("product/reviews/<slug:slug>", ReviewsListView.as_view(), name="all_product_review")

]