from django.urls import path
from .views import ProductCreateView, ReviewCreateView

urlpatterns = [
    path("new-product", ProductCreateView.as_view(), name="create_product"),
    path("new-review", ReviewCreateView.as_view(), name="review_product")
]