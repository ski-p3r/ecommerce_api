from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem
from .serializers import (CartCreateSerializer, CartItemSerializer, CartSerializer,
    CreateCartItemSerializer, UpdateCartItemSerializer)

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CartCreateSerializer
        return CartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CartItemViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCartItemSerializer
        elif self.action == 'update':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_queryset(self):
        cart_pk = self.kwargs.get('cart_pk')
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except Cart.DoesNotExist:
            return CartItem.objects.none()
        return CartItem.objects.filter(cart=cart)
    
    def get_serializer_context(self):
        cart_pk = self.kwargs.get('cart_pk')
        if cart_pk is not None:
            return {'cart_pk': cart_pk}
        return {}

    