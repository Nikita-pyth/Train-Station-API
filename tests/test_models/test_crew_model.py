from django.test import TestCase

from journeys.models import Crew


class CrewModelTest(TestCase):
    def setUp(self):
        self.crew = Crew.objects.create(first_name="testname", last_name="testsurname")

    def test_crew_created(self):
        crew = Crew.objects.first()
        self.assertEqual(crew, self.crew)
