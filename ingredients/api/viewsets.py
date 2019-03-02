from rest_framework.viewsets import ModelViewSet
from ingredients.models import Ingredient
from .serializers import IngredientSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
