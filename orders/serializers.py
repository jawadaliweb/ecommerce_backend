
from .models import Customer,Order,order_item
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ['id','name','password', 'email','billing_address','default_shipping_address','country', 'phone']


class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'shipping_address','order_address']



class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_price')
    def get_price(self, obj):
        return obj.quantity * obj.product.price
    class Meta:
        model = order_item
        fields = ['id','product','quantity', 'price']

    def create(self, validated_data):
        order_id = self.context['order_id']
        return order_item.objects.create(order_id=order_id, **validated_data)


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    items = OrderItemSerializer(read_only=True, many=True)
    quantity = serializers.SerializerMethodField('get_quantity')
    total_price = serializers.SerializerMethodField('get_total_price')
    def get_quantity(self, obj):
        total = 0 
        for item in obj.items.all():
            total += item.quantity
        return total
    def get_total_price(self, obj):
        return sum([ item.product.price * item.quantity for item in obj.items.all()])

    class Meta:
        model = Order
        fields = ['id','customer', 'items', 'amount','shipping_address','order_address','orderdate', 'quantity', 'total_price']
