from rest_framework.serializers import ModelSerializer
from items.models import Item
from ingredients.api.serializers import IngredientSerializer


class ItemSerializer(ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = ['ingredient', 'amount']
