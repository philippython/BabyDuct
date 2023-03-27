from django.shortcuts import render
import requests
from rest_framework import generics
from .models import Orders
from .serializers import OrderingServiceSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response

class OrderingServiceCreateView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceSingleView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceUpdateView(generics.UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

class OrderingServiceDeleteView(generics.DestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer


class OrderingServiceListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderingServiceSerializer

@api_view(['GET','POST'])
def completed_order(request,pk):
    complete = Orders.objects.all()
"""
def order_tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        try:
            order= Order.objects.filter(pk=orderId)

            if len(order)>0:
                update = Order.objects.filter(pk=orderId)
                updates = []
                for order in update:
                    order.status = 'Scheduled'
                    order.save()
                    updates.append({'status' : order.status})
                    response = json.dumps(updates)
                    return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,"tracker.html")
if the payment status is pending. And then fetch the orders object to get the pending objects

Orders.objects.filter(status=Orders.PENDING)
Once you iterate through this queryset you can hit payment_status_check request for a particular id and update the status again through

status=Orders.SUCCESS
"""