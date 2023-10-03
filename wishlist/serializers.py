from rest_framework import serializers
from shop.models import Product
from .models import Wishlist, WishlistItem

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class WishlistItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product = SimpleProductSerializer()
    class Meta:
        model = WishlistItem
        fields = ['id', 'product']

class WishlistSerializer(serializers.ModelSerializer):
    items = WishlistItemSerializer(many=True)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['items',]
