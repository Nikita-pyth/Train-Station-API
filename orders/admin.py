from django.contrib import admin
from orders.models import Order, Ticket


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["user__username"]
    inlines = [TicketInline]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "journey", "cargo", "seat", "order"]
    list_filter = ["journey", "cargo"]
    search_fields = [
        "journey__route__source__name",
        "journey__route__destination__name",
        "order__user__username",
    ]
