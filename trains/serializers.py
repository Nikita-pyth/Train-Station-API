from rest_framework import serializers
from trains.models import Train, TrainType


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = ['id', 'name']


class TrainSerializer(serializers.ModelSerializer):
    train_type = TrainTypeSerializer(read_only=True)

    class Meta:
        model = Train
        fields = ['id', 'name', 'cargo_num', 'places_in_cargo', 'train_type']
