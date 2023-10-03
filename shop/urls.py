from rest_framework_nested import routers
from . import views

router=routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('categories', views.CategoryViewSet, basename='category')
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('ratings', views.ReviewViewSet, basename='product-rates')

urlpatterns = router.urls + product_router.urls