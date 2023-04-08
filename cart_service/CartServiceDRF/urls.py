from django.urls import path
from . import views

urlpatterns = [
    path('carts/<str:slug>/create', views.CartCreateView.as_view(), name='create_cart'),
    #path('carts/<str:slug>/create', views.CartRetrieveView.as_view(), name='create_cart')
    path("cart-item/<int:pk>/update", views.CartItemUpdateView.as_view(), name="update_cart_item"),
    path("cart-item/<int:pk>/delete", views.CartItemDeleteView.as_view(), name="delete_cart_item"),
    path("cart-item/<int:pk>/retrieve", views.CartItemRetrieveView.as_view(), name="retrieve_cart_item"),
]