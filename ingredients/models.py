from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    desc = models.TextField(null=True, blank=True)
    unity_cost = models.DecimalField(max_digits=5, decimal_places=2)
    unity = models.CharField(max_length=20)

    def __str__(self):
        return self.name
