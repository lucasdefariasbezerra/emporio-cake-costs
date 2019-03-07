from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from cake.models import Cake
from .serializers import CakeSerializer
from .cakeService import CakeService
from cake_cost.dto.cake_dto import CakeDTO
from rest_framework.response import Response


class CakeViewSet(ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer

    def create(self, request, *args, **kwargs):
        cake_dto = CakeDTO(request.data['name'], request.data['description'])
        cake_dto.add_items(request.data['items'])
        service = CakeService()
        response = service.create_cake(cake_dto)
        if response == 1:
            return Response({'body': 'cake created with success'}, status=200)
        else:
            return Response({'body': 'error on creating cake'}, status=400)

    def partial_update(self, request, *args, **kwargs):
        service = CakeService()
        body = service.check_fields(request.data)
        if body['name'] or body['description']:
            cake_dto = CakeDTO(request.data['name'], request.data['description'])
            cake_id = kwargs['pk']
            response = service.update_cake(cake_dto, cake_id)
            if response == 1:
                return Response({'body': 'cake updated successfully'}, status=200)
            else:
                return Response({'body': 'error on cake update'}, status=400)

    @action(methods=['post'], detail=True)
    def add_items(self, request, pk=None):
        service = CakeService()
        cake_dto = CakeDTO(None, None, [])
        cake_dto.add_items(request.data['items'])
        response = service.add_cake_items(cake_dto, pk)
        if response == 1:
            return Response({'body': 'item was added on cake'}, status=200)
        else:
            return Response({'body': 'failure on item addition'}, status=400)
