from django.test import TestCase
from ingredients.models import Ingredient
from cake.models import Cake
from items.models import Item
from cake.api.cakeService import CakeService
from cake_cost.dto.cake_dto import CakeDTO
from cake_cost.dto.item_dto import ItemDTO


class TestCakeService(TestCase):
    cake_service = None

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='leite condensado', desc='leitte destilado', unity_cost=2,unity='un')
        self.ingredient2 = Ingredient.objects.create(name='leite em pó', desc='', unity_cost=1, unity='un')
        self.i1 = Item.objects.create(amount=1, ingredient=self.ingredient1)
        self.i2 = Item.objects.create(amount=1, ingredient=self.ingredient2)
        self.cake = Cake.objects.create(name='bolo de leite', description='teste desc')
        self.cake.items.add(self.i1)
        self.cake.items.add(self.i2)
        self.cake_service = CakeService()

    def test_create_cake_plain(self):
        cake_dto = CakeDTO('chocolate', 'bolo de chocolate')
        response = self.cake_service.create_cake(cake_dto)
        self.assertEqual(response, 1)

    def test_create_cake_with_items(self):
        items = [ItemDTO(self.ingredient1.pk, 2), ItemDTO(self.ingredient2.pk, 2)]
        cake = CakeDTO('leite condensado', 'bole de leite condensado', items)
        response = self.cake_service.create_cake(cake)
        self.assertEqual(response, 1)

    def test_create_cake_with_unexistent_ingredient(self):
        items = [ItemDTO(233, 22)]
        cake = CakeDTO('leite condensado', 'bole de leite condensado', items)
        response = self.cake_service.create_cake(cake)
        self.assertEqual(response, 0)

    def test_update_cake(self):
        cake_dto = CakeDTO('chocolate update', 'bolo de chocolate update')
        response = self.cake_service.update_cake(cake_dto, self.cake.pk)
        self.assertEqual(response, 1)

    def test_update_cake_fail(self):
        cake_dto = CakeDTO('chocolate update', 'bolo de chocolate update')
        response = self.cake_service.update_cake(cake_dto, 22)
        self.assertEqual(response, 0)

    def test_add_cake_items(self):
        items = [ItemDTO(self.ingredient1.pk, 2), ItemDTO(self.ingredient2.pk, 2)]
        cake = CakeDTO(None, None, items)
        response = self.cake_service.add_cake_items(cake, self.cake.pk)
        self.assertEqual(response, 1)

    def test_add_none_cake_item(self):
        response = self.cake_service.add_cake_items(None, self.cake.pk)
        self.assertEqual(response, 0)

    def test_add_inexistent_cake_item(self):
        response = self.cake_service.add_cake_items(None, self.cake.pk)
        self.assertEqual(response, 0)

    def test_check_field(self):
        request = self.cake_service.check_fields({})
        self.assertIsNone(request['name'])
        self.assertIsNone(request['description'])


