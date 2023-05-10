from django.urls import path
from .views import *

app_name = "orders"

urlpatterns = [
    path('create-order/',OrderingServiceCreateView.as_view(),name="create"),
    path('delete-order/<int:pk>/',OrderingServiceDeleteView.as_view(),name="delete"),
    path('cancel-order/<int:pk>/',OrderUpdateView.as_view(),name="update"),
    path('view-order/<int:pk>/',OrderingServiceSingleView.as_view(),name="view"),
    path('view-orders/',OrderingServiceListView.as_view(),name="views"),
    #path('view-completed-order',)
]