from rest_framework_nested import routers
from .views import CartViewSet, CartItemViewSet


router = routers.DefaultRouter()
router.register('', CartViewSet, basename='cart')
cart_router = routers.NestedDefaultRouter(router, '', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + cart_router.urls