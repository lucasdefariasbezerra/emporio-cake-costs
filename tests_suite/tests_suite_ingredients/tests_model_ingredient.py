from django.test import TestCase
from ingredients.models import Ingredient


# This test case will test the ingredient model.
class IngredientTestCases(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='leite condensado', desc='leitte destilado', unity_cost=2, unity='un')
        self.ingredient2 = Ingredient.objects.create(name='leite em pó', desc='', unity_cost=1, unity='un')

    def test_query_all(self):
        query = Ingredient.objects.all()
        self.assertEqual(query.count(), 2)

    def test_query_one(self):
        ingredient = Ingredient.objects.get(name='leite em pó')
        self.assertEqual(ingredient.name, 'leite em pó')

    def test_add_ingredient(self):
        Ingredient.objects.create(name='leite', desc='', unity_cost=3, unity='lt')
        count = Ingredient.objects.all().count()
        self.assertEqual(count, 3)

    def test_update_ingredient(self):
        ingredient = Ingredient.objects.get(name='leite condensado')
        ingredient.desc = 'update desc'
        ingredient.save()
        self.assertEqual(ingredient.desc, 'update desc')
