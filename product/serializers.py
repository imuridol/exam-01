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
    owner_full_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ('__all__')

    def get_owner_full_name(self, obj):
        return f'{obj.user.username}'

    def get_category_name(self, obj):
        return f'{obj.category.name}'



