from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order
from orders.models import Ticket
from journeys.models import Journey
from journeys.models import Route
from trains.models import Train, TrainType
from stations.models import Station
from datetime import datetime, timedelta

User = get_user_model()


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="orderuser", password="testpass")

        self.station_a = Station.objects.create(
            name="Riga", latitude=56.95, longitude=24.11
        )
        self.station_b = Station.objects.create(
            name="Daugavpils", latitude=55.87, longitude=26.52
        )
        self.route = Route.objects.create(
            source=self.station_a, destination=self.station_b, distance=230
        )

        self.train_type = TrainType.objects.create(name="Express")
        self.train = Train.objects.create(
            name="Train B", cargo_num=3, places_in_cargo=15, train_type=self.train_type
        )

        self.journey = Journey.objects.create(
            route=self.route,
            train=self.train,
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=3),
        )

        self.order = Order.objects.create(user=self.user)

    def test_order_creation(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.order.user.username, "orderuser")

    def test_order_ticket_relationship(self):
        ticket = Ticket.objects.create(
            journey=self.journey, cargo=1, seat=5, order=self.order
        )
        self.assertEqual(self.order.tickets.count(), 1)
        self.assertEqual(self.order.tickets.first(), ticket)
