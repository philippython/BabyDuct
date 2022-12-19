from django.urls import path
from .views import  *

urlpatterns = [

    # products endpoints
    path("products/<slug:slug>", ProductDetailView.as_view(), name="single_product"),
    path("product/<slug:slug>/edit", ProductUpdateView.as_view(), name="edit_product"),
    path("product/<slug:slug>/delete", ProductDeleteView.as_view(), name="delete_product"),
    path("product/new-product", ProductCreateView.as_view(), name="create_product"),
    path("all-products", ProductListView.as_view(), name="all_products"),
    
    # reviews endpoints
    path("product/review-create", ReviewCreateView.as_view(), name="review_product"),
    path("product/reviews/<slug:slug>", ReviewsListView.as_view(), name="all_product_review"),
    path("product/reviews/<slug:slug>/edit", ReviewUpdateView.as_view(), name="update_review"),
    path("product/reviews/<slug:slug>/delete", ReviewDeleteView.as_view(), name="delete_review"),
    path("product/user-reviews/<slug:slug>", UserReviewsListView.as_view(), name="all_product_review")

]