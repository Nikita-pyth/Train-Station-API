from django.test import TestCase
from orders.models import Ticket
from journeys.models import Journey
from orders.models import Order
from trains.models import Train, TrainType
from stations.models import Route, Station
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()

class TicketModelTest(TestCase):
    def setUp(self):
        self.station_a = Station.objects.create(name="Kyiv", latitude=50.45, longitude=30.52)
        self.station_b = Station.objects.create(name="Lviv", latitude=49.84, longitude=24.03)
        self.route = Route.objects.create(source=self.station_a, destination=self.station_b, distance=500)
        self.traintype = TrainType.objects.create(name="Fast")
        self.train = Train.objects.create(name="Train A", cargo_num=5, places_in_cargo=20, train_type=self.traintype)
        self.journey = Journey.objects.create(route=self.route, train=self.train,
                                              departure_time=datetime.now(),
                                              arrival_time=datetime.now() + timedelta(hours=5))
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.order = Order.objects.create(user=self.user)

    def test_ticket_creation(self):
        ticket = Ticket.objects.create(journey=self.journey, cargo=1, seat=10, order=self.order)
        self.assertEqual(ticket.cargo, 1)
        self.assertEqual(ticket.seat, 10)
        self.assertEqual(ticket.journey, self.journey)

    def test_ticket_unique_constraint(self):
        Ticket.objects.create(journey=self.journey, cargo=1, seat=10, order=self.order)
        with self.assertRaises(Exception):
            Ticket.objects.create(journey=self.journey, cargo=1, seat=10, order=self.order)
