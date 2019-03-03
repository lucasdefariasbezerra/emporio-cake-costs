from rest_framework.serializers import ModelSerializer
from items.api.serializers import ItemSerializer
from cake.models import Cake


class CakeSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cake
        fields = ['id', 'name', 'description', 'items']
