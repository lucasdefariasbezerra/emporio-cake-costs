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
        name = None
        description = None
        if request.data['name']:
            name = request.data['name']
        if request.data['description']:
            description = request.data['description']
        cake_dto = CakeDTO(name, description)

        if name or description:
            service = CakeService()
            cake_id = kwargs['pk']
            response = service.update_cake(cake_dto, cake_id)
            if response == 1:
                return Response({'body': 'cake updated successfully'}, status=200)
            else:
                return Response({'body': 'error on cake update'}, status=400)


