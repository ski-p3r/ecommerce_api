from rest_framework_nested import routers
from .views import CartViewSet, CartItemViewSet


router = routers.DefaultRouter()
router.register('carts', CartViewSet, basename='cart')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + cart_router.urls