from datetime import datetime

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.viewsets import ModelViewSet
from orders.models import Ticket, Order
from orders.serializers import TicketSerializer, OrderReadSerializer, OrderCreateSerializer


from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

@extend_schema_view(
    list=extend_schema(
        summary="List user tickets",
        parameters=[
            OpenApiParameter(
                "date", type=str,
                description="Filter by journey date (YYYY-MM-DD)",
                required=False
            )
        ]
    ),
    retrieve=extend_schema(summary="Retrieve a specific ticket"),
    create=extend_schema(summary="Create a new ticket"),
    update=extend_schema(summary="Update a ticket"),
    partial_update=extend_schema(summary="Partially update a ticket"),
    destroy=extend_schema(summary="Delete a ticket"),
)
class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Ticket.objects.filter(order__user=self.request.user)
        date = self.request.query_params.get('date')
        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d').date()
                queryset = queryset.filter(date=date_obj)
            except ValueError:
                pass
        return queryset

    def perform_create(self, serializer):
        order = serializer.validated_data['order']
        if order.user != self.request.user:
            raise PermissionDenied("You can only create tickets for your own orders.")
        serializer.save()


@extend_schema_view(
    list=extend_schema(summary="List user orders"),
    retrieve=extend_schema(summary="Retrieve a specific order"),
    create=extend_schema(summary="Create a new order"),
    update=extend_schema(summary="Update an order"),
    partial_update=extend_schema(summary="Partially update an order"),
    destroy=extend_schema(summary="Delete an order"),
)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderReadSerializer
