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

    def create(self, validated_data):
        wishlist_pk = self.context['wishlist_pk']
        product = validated_data['product']

        # Check if the Wishlist item already exists
        try:
            wishlist_item = WishlistItem.objects.get(wishlist_id=wishlist_pk, product=product)
            if wishlist_item:
                return serializers.ValidationError("Already in wishlist")
        except WishlistItem.DoesNotExist:
            # If it doesn't exist, create a new wishlist item
            wishlist_item = WishlistItem.objects.create(wishlist_id=wishlist_pk, **validated_data)

        return wishlist_item
