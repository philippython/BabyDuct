from django.urls import path
from . import views

urlpatterns = [
    path("cart-item/<str:slug>/add", views.AddToCartView.as_view(), name="add_to_cart"),
    path("cart-item/<int:pk>/update", views.CartItemUpdateView.as_view(), name="update_cart_item"),
    path("cart-item/<int:pk>/delete", views.CartItemDeleteView.as_view(), name="delete_cart_item"),
    path("cart-item/<int:pk>/retrieve", views.CartItemRetrieveView.as_view(), name="retrieve_cart_item"),
]