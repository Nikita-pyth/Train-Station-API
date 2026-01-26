from django.test import TestCase
from journeys.models import Crew
from journeys.serializers import CrewSerializer


class CrewSerializerTest(TestCase):
    def setUp(self):
        self.crew = Crew.objects.create(first_name="Anna", last_name="Ivanova")

    def test_crew_serializer_output(self):
        serializer = CrewSerializer(self.crew)
        expected_data = {
            "id": self.crew.id,
            "first_name": "Anna",
            "last_name": "Ivanova",
        }
        self.assertEqual(serializer.data, expected_data)

    def test_crew_serializer_fields(self):
        serializer = CrewSerializer()
        self.assertCountEqual(
            serializer.fields.keys(), ["id", "first_name", "last_name"]
        )
