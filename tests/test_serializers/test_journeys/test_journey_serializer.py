from django.test import TestCase
from django.contrib.auth import get_user_model
from stations.models import Station, Route
from trains.models import TrainType, Train
from journeys.models import Journey, Crew
from journeys.serializers import JourneySerializer
from datetime import datetime, timedelta

User = get_user_model()


class JourneySerializerTest(TestCase):
    def setUp(self):
        self.station_a = Station.objects.create(
            name="Rīga", latitude=56.95, longitude=24.11
        )
        self.station_b = Station.objects.create(
            name="Daugavpils", latitude=55.87, longitude=26.52
        )
        self.route = Route.objects.create(
            source=self.station_a, destination=self.station_b, distance=230
        )

        self.train_type = TrainType.objects.create(name="Express")
        self.train = Train.objects.create(
            name="Train B", cargo_num=3, places_in_cargo=20, train_type=self.train_type
        )

        self.journey = Journey.objects.create(
            route=self.route,
            train=self.train,
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=3),
        )

        self.crew1 = Crew.objects.create(first_name="John", last_name="Doe")
        self.crew2 = Crew.objects.create(first_name="Alice", last_name="Smith")
        self.journey.crew.set([self.crew1, self.crew2])

    def test_journey_serializer_output(self):
        serializer = JourneySerializer(self.journey)
        data = serializer.data

        self.assertEqual(data["id"], self.journey.id)
        self.assertEqual(data["train"]["id"], self.train.id)
        self.assertEqual(len(data["crew"]), 2)
        self.assertEqual(data["crew"][0]["first_name"], "John")
        self.assertEqual(data["crew"][1]["last_name"], "Smith")
