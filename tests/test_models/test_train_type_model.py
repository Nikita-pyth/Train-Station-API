from django.test import TestCase
from trains.models import TrainType


class TrainTypeModelTest(TestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(name="Intercity")

    def test_train_type_creation(self):
        self.assertEqual(TrainType.objects.count(), 1)
        self.assertEqual(self.train_type.name, "Intercity")

    def test_train_type_str(self):
        self.assertEqual(str(self.train_type), "Intercity")
