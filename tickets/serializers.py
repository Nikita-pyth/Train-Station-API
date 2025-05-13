from rest_framework import serializers
from tickets.models import Ticket, Order


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["cargo", "seat", "journey", "order",]


class OrderReadSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['created_at', 'tickets']
        read_only_fields = ['created_at', 'tickets']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id"]
