from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'detail', 'specs', 'subcategory', 'brand', 'status', 'is_featured')