from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journeys.views import JourneyViewSet, CrewViewSet

router = DefaultRouter()
router.register(r"journeys", JourneyViewSet, basename="journey")
router.register(r"crew", CrewViewSet, basename="crew")

urlpatterns = [
    path("", include(router.urls)),
]
