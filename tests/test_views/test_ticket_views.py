from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from orders.models import Ticket, Order
from journeys.models import Journey
from trains.models import Train, TrainType
from stations.models import Route, Station
from datetime import datetime, timedelta

User = get_user_model()


class TicketViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", email="other@example.com", password="testpass123"
        )

        self.station_a = Station.objects.create(name="A", latitude=0, longitude=0)
        self.station_b = Station.objects.create(name="B", latitude=1, longitude=1)
        self.route = Route.objects.create(
            source=self.station_a, destination=self.station_b, distance=100
        )
        self.train_type = TrainType.objects.create(name="Fast")
        self.train = Train.objects.create(
            name="Train 1", cargo_num=2, places_in_cargo=5, train_type=self.train_type
        )
        self.journey = Journey.objects.create(
            route=self.route,
            train=self.train,
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2),
        )

        self.order = Order.objects.create(user=self.user)
        self.other_order = Order.objects.create(user=self.other_user)

        self.ticket = Ticket.objects.create(
            journey=self.journey, cargo=1, seat=1, order=self.order
        )

        self.client.force_authenticate(user=self.user)
        self.list_url = reverse("ticket-list")
        self.detail_url = reverse("ticket-detail", args=[self.ticket.id])

    def test_list_user_tickets(self):
        Ticket.objects.create(
            journey=self.journey, cargo=2, seat=1, order=self.other_order
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["cargo"], 1)

    def test_create_ticket_for_own_order(self):
        payload = {
            "journey": self.journey.id,
            "cargo": 1,
            "seat": 2,
            "order": self.order.id,
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2)

    def test_create_ticket_for_other_user_order(self):
        payload = {
            "journey": self.journey.id,
            "cargo": 1,
            "seat": 3,
            "order": self.other_order.id,
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Ticket.objects.count(), 1)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
