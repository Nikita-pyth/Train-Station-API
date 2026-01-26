from django.test import TestCase
from trains.models import Train, TrainType


class TrainModelTest(TestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(name="Regional")
        self.train = Train.objects.create(
            name="Train X", cargo_num=5, places_in_cargo=30, train_type=self.train_type
        )

    def test_train_creation(self):
        self.assertEqual(Train.objects.count(), 1)
        self.assertEqual(self.train.name, "Train X")
        self.assertEqual(self.train.cargo_num, 5)
        self.assertEqual(self.train.places_in_cargo, 30)
        self.assertEqual(self.train.train_type, self.train_type)

    def test_train_str(self):
        self.assertEqual(str(self.train), "Train X")
