from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer() # Вложенный сериализатор

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'product', 'author', 'rating', 'comment', 'created_at']
