from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, GetCategorySerializer, ProductSerializer

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