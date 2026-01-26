from rest_framework import serializers
from stations.models import Station, Route


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ["name", "latitude", "longitude"]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ["source", "destination", "distance"]
