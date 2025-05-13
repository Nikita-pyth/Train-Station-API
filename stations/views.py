from rest_framework.viewsets import ModelViewSet
from stations.models import Station, Route
from stations.serializers import StationSerializer, RouteSerializer

class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
