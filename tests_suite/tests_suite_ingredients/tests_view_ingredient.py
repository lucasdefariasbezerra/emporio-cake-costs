from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from ingredients.models import Ingredient


class IngredientViewTest(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='leite condensado', desc='leitte destilado', unity_cost=2, unity='un')
        self.ingredient2 = Ingredient.objects.create(name='leite em pó', desc='', unity_cost=1, unity='un')

    def test_ingredient_get(self):
        url = reverse('ingredients-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ingredient_detail(self):
        url = reverse('ingredients-detail', kwargs={'pk': self.ingredient1.pk})
        response = self.client.get(url)
        actual_name = response.data['name']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(actual_name, 'leite condensado')
