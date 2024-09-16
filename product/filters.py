from django_filters import rest_framework as filters
from .models import ProductModel

class ProductFilter(filters.FilterSet):
    class Meta:
        model = ProductModel
        fields = ('category', )
