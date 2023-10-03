from rest_framework import serializers
from .models import Category, Product, Review
from authentication.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']

class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data

class GetCategorySerializer(serializers.ModelSerializer):
    children = RecursiveCategorySerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'children', 'product_count']

    def get_product_count(self, instance):
        # Count the number of products related to this category
        return instance.products.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        children = instance.children.all()

        if not children:
            data.pop('children')
        else:
            # Count the number of products for all child categories
            child_product_count = sum(child.products.count() for child in children)
            data['product_count'] += child_product_count

        return data

class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    category = SimpleCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class SimpleUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = SimpleUserSerializer(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'comment', 'updated_at', 'rating']


    def create(self, validated_data):
        product_pk = self.context['product_pk']
        user = self.context['user']

        review = Review.objects.create(product_id=product_pk, user=user, **validated_data)

        return review