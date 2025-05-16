from django.urls import path, include
from rest_framework.routers import DefaultRouter
from trains.views import TrainViewSet, TrainTypeViewSet

router = DefaultRouter()
router.register(r"trains", TrainViewSet, basename="train")
router.register(r"types", TrainTypeViewSet, basename="train-type")

urlpatterns = [
    path("", include(router.urls)),
]
