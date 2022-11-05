from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('category', views.CategoryViewSet)


products_routers = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_routers.register('images',views.ImageViewSet, basename='Product_Images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_routers.urls)),
]
