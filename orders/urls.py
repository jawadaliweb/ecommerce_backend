from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)


items_routers = routers.NestedDefaultRouter(router, 'orders', lookup='order')
items_routers.register('items',views.OrderItemViewSet, basename='order-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(items_routers.urls)),

]
