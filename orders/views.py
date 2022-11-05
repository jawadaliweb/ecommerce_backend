from .models import Customer,Order,order_item
from products.models import Product
from .serializers import *
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
   
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerSerializer


class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Order.objects.select_related('customer').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return PostOrderSerializer

    def get_queryset(self):
        customer = self.request.query_params.get('customer')
        if customer is not None:
            return Order.objects.select_related('customer','order_id').filter(customer=customer)
        return Order.objects.select_related('customer').prefetch_related('items__product').all()

class OrderItemViewSet(viewsets.ModelViewSet):
    # queryset = order_item.objects.all()
    serializer_class = OrderItemSerializer
 
    def get_queryset(self):
        return order_item.objects.select_related('product').filter(order_id=self.kwargs['order_pk'])

    def get_serializer_context(self):
        return {'order_id':self.kwargs['order_pk']}
    