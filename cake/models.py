from django.db import models
from items.models import Item


# Create your models here.
class Cake(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        self.name
