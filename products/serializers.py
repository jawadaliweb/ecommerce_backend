
from unicodedata import category
from .models import Product,Category,ProductImage
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','thumbnail']
        depth=1

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','image']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price', 'weight','description','thumbnail','create_date', 'category', 'images']

class PostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price', 'weight','description','thumbnail','create_date', 'category']


