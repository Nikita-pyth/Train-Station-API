from drf_spectacular.utils import extend_schema, OpenApiParameter

ticket_schema = {
    "list": extend_schema(
        summary="List user tickets",
        parameters=[
            OpenApiParameter(
                "date",
                type=str,
                description="Filter by journey date (YYYY-MM-DD)",
                required=False,
            )
        ],
    ),
    "retrieve": extend_schema(summary="Retrieve a specific ticket"),
    "create": extend_schema(summary="Create a new ticket"),
    "update": extend_schema(summary="Update a ticket"),
    "partial_update": extend_schema(summary="Partially update a ticket"),
    "destroy": extend_schema(summary="Delete a ticket"),
}

order_schema = {
    "list": extend_schema(summary="List user orders"),
    "retrieve": extend_schema(summary="Retrieve a specific order"),
    "create": extend_schema(summary="Create a new order"),
    "update": extend_schema(summary="Update an order"),
    "partial_update": extend_schema(summary="Partially update an order"),
    "destroy": extend_schema(summary="Delete an order"),
}
