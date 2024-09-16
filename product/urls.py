from django.urls import path, include
from rest_framework import routers
from .views import *


urlpatterns = [
    # path('', include(router.urls))
    path('categories/', CategoryListCreate.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view()),
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]