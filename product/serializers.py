from rest_framework import serializers
from .models import ProductModel
from category.models import CategoryModel
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price', 'owner', 'category']


