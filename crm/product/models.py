from django.db import models
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    min_quantity = models.PositiveIntegerField(null=True, blank=True)
    cost = models.PositiveIntegerField(null=True, blank=True)
    cost_per_unit = models.PositiveIntegerField(null=True, blank=True)
    delivered_date = models.DateField(null=True, blank=True)
    best_before = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

