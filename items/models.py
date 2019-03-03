from django.db import models
from ingredients.models import Ingredient


# Create your models here.
class Item(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.ingredient.name + ' ' + self.amount

