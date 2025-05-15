from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order, Ticket
from stations.models import Station, Route
from trains.models import TrainType, Train
from journeys.models import Journey
from orders.serializers import TicketSerializer
from datetime import datetime, timedelta

User = get_user_model()

class TicketSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.station_a = Station.objects.create(name="A", latitude=0, longitude=0)
        self.station_b = Station.objects.create(name="B", latitude=1, longitude=1)
        self.route = Route.objects.create(source=self.station_a, destination=self.station_b, distance=100)
        self.train_type = TrainType.objects.create(name="Fast")
        self.train = Train.objects.create(name="Train 1", cargo_num=2, places_in_cargo=5, train_type=self.train_type)
        self.journey = Journey.objects.create(route=self.route, train=self.train,
                                              departure_time=datetime.now(),
                                              arrival_time=datetime.now() + timedelta(hours=2))
        self.order = Order.objects.create(user=self.user)

    def test_valid_ticket(self):
        data = {
            "cargo": 1,
            "seat": 3,
            "journey": self.journey.id,
            "order": self.order.id
        }
        serializer = TicketSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_invalid_cargo(self):
        data = {
            "cargo": 5,
            "seat": 2,
            "journey": self.journey.id,
            "order": self.order.id
        }
        serializer = TicketSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("cargo", serializer.errors)

    def test_invalid_seat(self):
        data = {
            "cargo": 1,
            "seat": 999,
            "journey": self.journey.id,
            "order": self.order.id
        }
        serializer = TicketSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("seat", serializer.errors)
