from django.test import TestCase
from stations.models import Station, Route
from stations.serializers import RouteSerializer


class RouteSerializerTest(TestCase):
    def setUp(self):
        self.station_a = Station.objects.create(
            name="Rīga", latitude=56.95, longitude=24.11
        )
        self.station_b = Station.objects.create(
            name="Liepāja", latitude=56.51, longitude=21.01
        )
        self.route = Route.objects.create(
            source=self.station_a, destination=self.station_b, distance=210
        )

    def test_route_serializer_output(self):
        serializer = RouteSerializer(instance=self.route)
        data = serializer.data
        self.assertEqual(data["distance"], 210)
        self.assertEqual(data["source"], self.station_a.id)
        self.assertEqual(data["destination"], self.station_b.id)

    def test_route_serializer_fields(self):
        serializer = RouteSerializer()
        self.assertCountEqual(
            serializer.fields.keys(), ["source", "destination", "distance"]
        )
