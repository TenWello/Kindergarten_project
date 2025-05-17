from django.db import models
from meal.models import Meal
from product.models import product

class Ingredient(models.Model):
    meal_id = models.ForeignKey('Meal', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    quantity_per_portion = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name