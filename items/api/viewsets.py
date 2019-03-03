from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from items.models import Item
from .serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # this create will invalidate the items creations in the items api
    # it will be cake API responsability
    def create(self, request, *args, **kwargs):
        return Response({'message': 'this resource is not enabled to create items'})

    def update(self, request, *args, **kwargs):
        return Response({'message': 'this resource is not enabled to update items'})

    def partial_update(self, request, *args, **kwargs):
        return Response({'message': 'this resource is not enabled to partially update items'})

    def destroy(self, request, *args, **kwargs):
        return Response({'message': 'this resource is not enabled to delete items'})
