from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Wishlist, WishlistItem
from .serializers import WishlistSerializer, WishlistItemSerializer, WishlistItemCreateSerializer

# Create your views here.

class WishListViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class WishlistItemViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return WishlistItemCreateSerializer
        return WishlistItemSerializer
    def get_queryset(self):
        wishlist_pk = self.kwargs.get('wishlist_pk')
        try:
            wishlist = Wishlist.objects.get(pk=wishlist_pk)
        except Wishlist.DoesNotExist:
            return Wishlist.objects.none()
        return WishlistItem.objects.filter(wishlist=wishlist)
    
    def get_serializer_context(self):
        wishlist_pk = self.kwargs.get('wishlist_pk')
        if wishlist_pk is not None:
            return {'wishlist_pk': wishlist_pk}
        return {}