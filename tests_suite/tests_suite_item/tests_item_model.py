from django.test import TestCase
from ingredients.models import Ingredient
from items.models import Item


# This test case will test the item model.
class ItemTestCases(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='leite condensado', desc='leitte destilado', unity_cost=2, unity='un')
        self.ingredient2 = Ingredient.objects.create(name='leite em pó', desc='', unity_cost=1, unity='un')
        self.i1 = Item.objects.create(amount=1, ingredient=self.ingredient1)
        self.i2 = Item.objects.create(amount=1, ingredient=self.ingredient2)

    def test_query_all(self):
        query = Item.objects.all()
        self.assertEqual(query.count(), 2)

    def test_query_one(self):
        item = Item.objects.get(id=self.i1.pk)
        self.assertEqual(item.ingredient.name, 'leite condensado')
        self.assertEqual(item.amount, 1)

    def test_add_ingredient(self):
        ingredient = Ingredient(name='leite', desc='', unity_cost=3, unity='lt')
        ingredient.save()
        Item.objects.create(amount=0.2, ingredient=ingredient)
        count = Item.objects.count()
        self.assertEqual(count, 3)

    # def test_update_ingredient(self):
    #    ingredient = Ingredient.objects.get(name='leite condensado')
    #    ingredient.desc = 'update desc'
    #    ingredient.save()
    #   self.assertEqual(ingredient.desc, 'update desc')