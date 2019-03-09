from django.test import TestCase
from ingredients.models import Ingredient
from items.models import Item
from cake.models import Cake


# This test case will test the cake model.
class ItemTestCases(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='leite condensado', desc='leitte destilado', unity_cost=2, unity='un')
        self.ingredient2 = Ingredient.objects.create(name='leite em pó', desc='', unity_cost=1, unity='un')
        self.i1 = Item.objects.create(amount=1, ingredient=self.ingredient1)
        self.i2 = Item.objects.create(amount=1, ingredient=self.ingredient2)
        self.cake = Cake.objects.create(name='bolo de leite', description='teste desc')
        self.cake.items.add(self.i1)
        self.cake.items.add(self.i2)

    def test_query_all(self):
        query = Cake.objects.all()
        self.assertEqual(query.count(), 1)

    def test_query_one(self):
        cake = Cake.objects.get(id=self.cake.pk)
        self.assertEqual(cake.name, 'bolo de leite')

    def test_add_cake(self):
        ingredient = Ingredient(name='leite', desc='', unity_cost=3, unity='lt')
        ingredient.save()
        item1 = Item.objects.create(amount=0.2, ingredient=ingredient)
        cake = Cake.objects.create(name='bolo 2', description='teste')
        cake.items.add(item1)
        cake.save()
        count = Cake.objects.count()
        self.assertEqual(count, 2)

    def test_update_ingredient(self):
        cake = Cake.objects.get(id=self.cake.pk)
        cake.desc = 'update desc'
        cake.save()
        self.assertEqual(cake.desc, 'update desc')
