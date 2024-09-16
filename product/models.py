from django.db import models
from category.models import *
from django.contrib.auth.models import User
# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
