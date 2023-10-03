from rest_framework import serializers
from shop.models import Product
from .models import Cart, CartItem

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total']

    def get_total(self, obj):
        return obj.product.price * obj.quantity

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['items', 'total_price']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())

class CartCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']

class CreateCartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("The quantity must be a positive integer.")
        return value

    def create(self, validated_data):
        cart_pk = self.context['cart_pk']
        product = validated_data['product']
        quantity = validated_data['quantity']

        # Check if the cart item already exists
        try:
            cart_item = CartItem.objects.get(cart_id=cart_pk, product=product)
            cart_item.quantity += quantity
            if cart_item.quantity < 1:
                cart_item.delete()
            else:
                cart_item.save()
        except CartItem.DoesNotExist:
            # If it doesn't exist, create a new cart item
            cart_item = CartItem.objects.create(cart_id=cart_pk, **validated_data)

        return cart_item

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("The quantity must be a positive integer.")
        return value

    def update(self, instance, validated_data):
        old_quantity = instance.quantity
        new_quantity = validated_data.get('quantity', old_quantity)

        # Update the quantity field
        instance.quantity = new_quantity
        instance.save()

        return instance