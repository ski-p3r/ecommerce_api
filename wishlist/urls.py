from rest_framework_nested import routers
from .views import WishListViewSet, WishlistItemViewSet


router = routers.DefaultRouter()
router.register('', WishListViewSet, basename='wishlist')
wishlist_router = routers.NestedDefaultRouter(router, '', lookup='wishlist')
wishlist_router.register('items', WishlistItemViewSet, basename='wishlist-items')

urlpatterns = router.urls + wishlist_router.urls