from django.contrib import admin
from .models import Journey, Crew


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ["route", "train", "departure_time", "arrival_time"]
    list_filter = ["route", "train", "departure_time"]
    search_fields = ["route__source__name", "route__destination__name", "train__name"]
    filter_horizontal = ["crew"]
