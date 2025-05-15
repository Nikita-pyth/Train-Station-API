from django.test import TestCase
from stations.models import Station, Route

class RouteModelTest(TestCase):
    def setUp(self):
        self.station_a = Station.objects.create(name="Rīga", latitude=56.95, longitude=24.11)
        self.station_b = Station.objects.create(name="Liepāja", latitude=56.51, longitude=21.01)

        self.route = Route.objects.create(
            source=self.station_a,
            destination=self.station_b,
            distance=210
        )

    def test_route_created(self):
        self.assertEqual(Route.objects.count(), 1)
        self.assertEqual(self.route.source, self.station_a)
        self.assertEqual(self.route.destination, self.station_b)
        self.assertEqual(self.route.distance, 210)

    def test_route_str(self):
        expected_str = f"{self.station_a} → {self.station_b}"
        self.assertEqual(str(self.route), expected_str)
