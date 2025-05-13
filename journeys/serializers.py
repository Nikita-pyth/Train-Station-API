from rest_framework import serializers
from journeys.models import Journey, Crew
from stations.serializers import RouteSerializer
from trains.serializers import TrainSerializer


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ['id', 'first_name', 'last_name']


class JourneySerializer(serializers.ModelSerializer):
    crew = CrewSerializer(many=True, read_only=True)
    route = RouteSerializer(read_only=True)
    train = TrainSerializer(read_only=True)

    class Meta:
        model = Journey
        fields = ['id', 'route', 'train', 'departure_time', 'arrival_time', 'crew']
