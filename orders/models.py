from itertools import product
from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    billing_address = models.TextField()
    default_shipping_address = models.TextField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class order_item(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    amount = models.IntegerField()
    shipping_address =  models.CharField(max_length=250, null=True, blank=True)
    order_address = models.CharField(max_length=250)
    orderdate = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.shipping_address :
            self.shipping_address = self.customer.default_shipping_address
        
        if not self.order_address:
            self.order_address = self.customer.billing_address
    
        super().save()
