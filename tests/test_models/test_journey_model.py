from django.test import TestCase
from journeys.models import Journey
from trains.models import Train, TrainType
from stations.models import Station, Route
from datetime import datetime, timedelta


class JourneyModelTest(TestCase):
    def setUp(self):
        self.station_a = Station.objects.create(
            name="Kyiv", latitude=50.45, longitude=30.52
        )
        self.station_b = Station.objects.create(
            name="Lviv", latitude=49.84, longitude=24.03
        )

        self.route = Route.objects.create(
            source=self.station_a, destination=self.station_b, distance=500
        )

        self.train_type = TrainType.objects.create(name="High-Speed")
        self.train = Train.objects.create(
            name="Train X", cargo_num=10, places_in_cargo=20, train_type=self.train_type
        )

        self.departure_time = datetime.now()
        self.arrival_time = self.departure_time + timedelta(hours=5)
        self.journey = Journey.objects.create(
            route=self.route,
            train=self.train,
            departure_time=self.departure_time,
            arrival_time=self.arrival_time,
        )

    def test_journey_created(self):
        self.assertEqual(self.journey.route, self.route)
        self.assertEqual(self.journey.train, self.train)
        self.assertEqual(self.journey.departure_time, self.departure_time)
        self.assertEqual(self.journey.arrival_time, self.arrival_time)

    def test_journey_str(self):
        self.assertIn("Kyiv → Lviv", str(self.journey))
