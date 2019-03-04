from cake.models import Cake
from items.models import Item
from ingredients.models import Ingredient


class CakeService:
    item_model = None
    cake_model = None

    def __init__(self, item_model=None, cake_model=None):
        self.item_model = item_model
        self.cake_model = cake_model

    def create_cake(self, cake_dto):
        try:
            self.cake_model = Cake.objects.create(name=cake_dto.name, description=cake_dto.description)
            for item in cake_dto.items:
                ingredient = Ingredient.objects.get(id=item.ingredient_id)
                self.item_model = Item.objects.create(amount=item.amount, ingredient=ingredient)
                self.cake_model.items.add(self.item_model)
            return 1
        except:
            return 0

    def update_cake(self, cake_dto, cake_id):
        try:
            self.cake_model = Cake.objects.get(id=cake_id)

            if cake_dto.name:
                self.cake_model.name = cake_dto.name

            if cake_dto.description:
                self.cake_model.description = cake_dto.description

            self.cake_model.save()
            return 1
        except:
            return 0

    def add_cake_items(self, cake_dto, cake_id):
        try:
            self.cake_model = Cake.objects.get(id=cake_id)
            for item in cake_dto.items:
                ingredient = Ingredient.objects.get(id=item.ingredient_id)
                self.item_model = Item.objects.create(amount=item.amount, ingredient=ingredient)
                self.cake_model.items.add(self.item_model)
            return 1
        except:
            return 0
