from rest_framework import serializers
from orders.models import Ticket, Order


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["cargo", "seat", "journey", "order",]

    def validate(self, data):
        journey = data.get("journey")
        cargo = data.get("cargo")
        seat = data.get("seat")

        train = journey.train

        if cargo < 1 or cargo > train.cargo_num:
            raise serializers.ValidationError({
                "cargo": f"Cargo must be between 1 and {train.cargo_num}."
            })

        if seat < 1 or seat > train.places_in_cargo:
            raise serializers.ValidationError({
                "seat": f"Seat must be between 1 and {train.places_in_cargo}."
            })

        return data

class OrderReadSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", 'created_at', 'tickets']
        read_only_fields = ['created_at', 'tickets']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id"]
