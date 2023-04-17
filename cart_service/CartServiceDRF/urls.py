from django.urls import path
from . import views

urlpatterns = [
    path('cart-item/list', views.CartItemListView.as_view(),name="list_cart"),
    path('cart-item/create', views.CartCreateView.as_view(),name="create_cart"),
    path("cart-item/<int:pk>/update", views.CartItemUpdateView.as_view(),name="update_cart"),
    path("cart-item/<int:pk>/delete", views.CartItemDeleteView.as_view(),name="delete_cart"),
    path("cart-item/<int:pk>/retrieve", views.CartItemRetrieveView.as_view(),name="retrieve_cart"),
]