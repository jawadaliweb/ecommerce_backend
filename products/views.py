from itertools import product
from rest_framework.decorators import api_view
from .models import Category, Product, ProductImage
from .serializers import ProductSerializer,CategorySerializer, ImageSerializer, PostProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, get_object_or_404
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').select_related('category').all()
   
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return PostProductSerializer

    def delete(self,request,id):
        product = get_object_or_404(Product,pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        return {'request':self.request}
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        instance = Product.objects.select_related('category').get(id=serializer.data['id'])
        GetSerializer = ProductSerializer(instance)
        return Response(GetSerializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    
    def get_queryset(self):
        return ProductImage.objects.filter(product=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
    