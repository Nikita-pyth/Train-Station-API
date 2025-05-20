from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from datetime import datetime

from drf_spectacular.utils import extend_schema_view

from orders.models import Ticket, Order
from orders.serializers import (
    TicketSerializer,
    OrderReadSerializer,
    OrderCreateSerializer,
)
from orders.schemas import ticket_schema, order_schema


@extend_schema_view(**ticket_schema)
class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Ticket.objects.filter(order__user=self.request.user)
        date = self.request.query_params.get("date")
        if date:
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d").date()
                queryset = queryset.filter(date=date_obj)
            except ValueError:
                pass
        return queryset

    def perform_create(self, serializer):
        order = serializer.validated_data["order"]
        if order.user != self.request.user:
            raise PermissionDenied("You can only create tickets for your own orders.")
        serializer.save()


@extend_schema_view(**order_schema)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return OrderReadSerializer
