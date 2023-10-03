from django.db import transaction
from rest_framework import serializers
from .models import Order, OrderItem
from cart.serializers import SimpleProductSerializer
from cart.models import CartItem

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    def get_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(order_items, many=True).data

    def get_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.order_items.all())  # Calculate the total here

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'address', 'created_at', 'items', 'total']

    def create(self, validated_data):
        cart = validated_data['cart']
        user = self.context['user']
        address = validated_data['address']

        # Check if the cart is not empty
        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty. Cannot create an order.")

        with transaction.atomic():
            # Create the order
            order = Order.objects.create(cart=cart, user=user, address=address)

            # Create order items from cart items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )
                product=cart_item.product
                product.quantity -= cart_item.quantity
                product.save()

            # Clear the cart items
            cart_items.delete()

        return order