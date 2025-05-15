from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order, Ticket
from orders.serializers import (
    OrderCreateSerializer,
    OrderReadSerializer,
)
from stations.models import Station, Route
from trains.models import TrainType, Train
from journeys.models import Journey
from datetime import datetime, timedelta

User = get_user_model()

class OrderSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.order = Order.objects.create(user=self.user)

        self.station_a = Station.objects.create(name="A", latitude=0, longitude=0)
        self.station_b = Station.objects.create(name="B", latitude=1, longitude=1)
        self.route = Route.objects.create(source=self.station_a, destination=self.station_b, distance=120)
        self.train_type = TrainType.objects.create(name="Bullet")
        self.train = Train.objects.create(name="Train Z", cargo_num=2, places_in_cargo=5, train_type=self.train_type)
        self.journey = Journey.objects.create(
            route=self.route,
            train=self.train,
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2)
        )

        self.ticket = Ticket.objects.create(journey=self.journey, cargo=1, seat=2, order=self.order)

    def test_order_create_serializer(self):
        serializer = OrderCreateSerializer(instance=self.order)
        self.assertEqual(serializer.data["id"], self.order.id)

    def test_order_read_serializer(self):
        serializer = OrderReadSerializer(instance=self.order)
        data = serializer.data
        self.assertIn("created_at", data)
        self.assertEqual(len(data["tickets"]), 1)
        self.assertEqual(data["tickets"][0]["seat"], 2)
        self.assertEqual(data["tickets"][0]["cargo"], 1)
