from django.urls import path
from . import views

urlpatterns = [
    path('cart-item/list', views.CartItemListView.as_view()),
    path('cart-item/create', views.CartCreateView.as_view()),
    path("cart-item/<int:pk>/update", views.CartItemUpdateView.as_view()),
    path("cart-item/<int:pk>/delete", views.CartItemDeleteView.as_view()),
    path("cart-item/<int:pk>/retrieve", views.CartItemRetrieveView.as_view()),
]