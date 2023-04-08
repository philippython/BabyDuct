from django.urls import path
from .views import OrderingServiceDeleteView,OrderingServiceSingleView,OrderingServiceUpdateView,OrderingServiceCreateView,OrderingServiceListView
urlpatterns = [
    path('create-order/',OrderingServiceCreateView.as_view()),
    path('delete-order/<int:pk/',OrderingServiceDeleteView.as_view()),
    path('update-order/<int:pk>/',OrderingServiceUpdateView.as_view()),
    path('view-order/<int:pk>/',OrderingServiceSingleView.as_view()),
    path('view-orders/',OrderingServiceListView.as_view()),
]