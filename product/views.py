from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductListview(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = DjangoFilterBackend