from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from stations.models import Station, Route
from stations.serializers import StationSerializer, RouteSerializer


@extend_schema(
    summary="Station CRUD",
    tags=["Station"]
)
class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


@extend_schema(
    summary="Route CRUD",
    tags=["Route"]
)
class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
