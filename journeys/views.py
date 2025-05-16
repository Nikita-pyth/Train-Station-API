from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from journeys.models import Journey, Crew
from journeys.serializers import JourneySerializer, CrewSerializer


@extend_schema(
    summary="Crew CRUD",
    tags=["Crew"],
)
class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


@extend_schema(
    summary="Journey CRUD",
    tags=["Journey"],
)
class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
