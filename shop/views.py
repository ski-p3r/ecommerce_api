from django_filters import rest_framework as filters
from rest_framework import status, permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, GetCategorySerializer, ProductSerializer, ReviewSerializer

# Create your views here.

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_name = filters.CharFilter(method='filter_category_name')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']

    def filter_category_name(self, queryset, name, value):
        return queryset.filter(category__name__icontains=value)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.select_related('parent').filter(parent=None)
    serializer_class = GetCategorySerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CategorySerializer
        elif self.action == 'list' or self.action == 'retrieve':
            return GetCategorySerializer
        return CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    permission_classes = [IsAdminUser | ReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class IsReviewCreatorForUpdate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allow updates only if the user is the creator of the review.
        return obj.user == request.user

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action in ['create', ]:
            return [permissions.IsAuthenticated()]
        return [IsReviewCreatorForUpdate()]

    def get_serializer_context(self):
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return {'product_pk': product_pk, 'user': self.request.user}
        return {}
    
    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return Review.objects.filter(product_id=product_pk)