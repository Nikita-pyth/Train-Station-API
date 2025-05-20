from django.conf import settings
from django.db import models
from journeys.models import Journey

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class Ticket(models.Model):
    cargo = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")

    class Meta:
        unique_together = ("journey", "cargo", "seat")

    def __str__(self):
        return f"Ticket #{self.id} for {self.journey}"
