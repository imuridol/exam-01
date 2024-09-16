from django_filters import rest_framework as filters
from .models import ProductModel
import django_filters

class ProductFilter(filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    in_stock = django_filters.BooleanFilter(field_name='in_stock')
    class Meta:
        model = ProductModel
        fields = ['category', 'min_price', 'max_price', 'in_stock']