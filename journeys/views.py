from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from journeys.models import Journey, Crew
from journeys.serializers import JourneySerializer, CrewSerializer


@extend_schema(
    summary="Crew CRUD",
    parameters=[
        OpenApiParameter("search", str, description="Optional name filter", required=False),
    ],
    tags=["Crew"]
)
class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    filter_backends = [SearchFilter,]
    search_fields = ['first_name', 'last_name']


@extend_schema(
    summary="Journey CRUD",
    parameters=[
        OpenApiParameter("date", str, description="Filter by departure date (YYYY-MM-DD)", required=False),
    ],
    tags=["Journey"]
)
class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    filter_backends = [SearchFilter,]
    search_fields = ["departure_date",]
