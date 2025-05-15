from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from orders.models import Order

User = get_user_model()

class OrderViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass123'
        )
        
        self.order = Order.objects.create(user=self.user)
        self.other_order = Order.objects.create(user=self.other_user)
        
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('order-list')
        self.detail_url = reverse('order-detail', args=[self.order.id])

    def test_list_user_orders(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_order(self):
        response = self.client.post(self.list_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 3)
        new_order = Order.objects.latest('id')
        self.assertEqual(new_order.user, self.user)

    def test_get_order_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('created_at', response.data)
        self.assertIn('tickets', response.data)

    def test_get_other_user_order_detail(self):
        other_order_url = reverse('order-detail', args=[self.other_order.id])
        response = self.client.get(other_order_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_order(self):
        response = self.client.patch(self.detail_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.filter(id=self.order.id).count(), 0)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_serializer_class_selection(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tickets', response.data['results'][0])
        self.assertIn('created_at', response.data['results'][0])

        response = self.client.post(self.list_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
