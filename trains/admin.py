from django.contrib import admin
from trains.models import Train, TrainType


@admin.register(TrainType)
class TrainTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ["name", "train_type", "cargo_num", "places_in_cargo"]
    list_filter = ["train_type"]
    search_fields = ["name"]
