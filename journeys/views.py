from rest_framework.viewsets import ModelViewSet
from journeys.models import Journey, Crew
from journeys.serializers import JourneySerializer, CrewSerializer


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
