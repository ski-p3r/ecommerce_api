from rest_framework_nested import routers
from .views import OrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()
router.register('', OrderViewSet, basename='order')
order_router = routers.NestedDefaultRouter(router, '', lookup='order')
order_router.register('items', OrderItemViewSet, basename='order-items')

urlpatterns = router.urls + order_router.urls