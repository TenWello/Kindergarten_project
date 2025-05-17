from django.db import models
from product.models import Product


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    delivery_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(null=True, blank=True)
    total = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
