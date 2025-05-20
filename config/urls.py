import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Application APIs
    path("api/stations/", include("stations.urls")),
    path("api/trains/", include("trains.urls")),
    path("api/journeys/", include("journeys.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/users/", include("users.urls")),

    # Debug Toolbar
    path("__debug__/", include(debug_toolbar.urls)),

    # API Schema & Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
