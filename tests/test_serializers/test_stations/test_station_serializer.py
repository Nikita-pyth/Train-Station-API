from django.test import TestCase
from stations.models import Station
from stations.serializers import StationSerializer


class StationSerializerTest(TestCase):
    def setUp(self):
        self.station = Station.objects.create(
            name="Rīga", latitude=56.95, longitude=24.11
        )

    def test_station_serializer_output(self):
        serializer = StationSerializer(instance=self.station)
        expected = {"name": "Rīga", "latitude": 56.95, "longitude": 24.11}
        self.assertEqual(serializer.data, expected)

    def test_station_serializer_fields(self):
        serializer = StationSerializer()
        self.assertCountEqual(
            serializer.fields.keys(), ["name", "latitude", "longitude"]
        )
