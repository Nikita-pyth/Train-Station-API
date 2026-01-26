from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from trains.models import Train, TrainType
from trains.serializers import TrainSerializer, TrainTypeSerializer


@extend_schema(summary="Train CRUD", tags=["Train"])
class TrainViewSet(ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


@extend_schema(summary="Train type CRUD", tags=["TrainType"])
class TrainTypeViewSet(ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
