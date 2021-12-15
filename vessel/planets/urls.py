from django.urls import path

from vessel.planet.views import (
    PlanetCreateView,
    PlanetDeleteView,
    PlanetDetailView,
    PlanetListView,
    PlanetUpdateView,
)

app_name = "categorias"

urlpatterns = [
    path("planets/",
        PlanetListView.as_view(),
        name="planet-list"
    ),

    path(
        "planet/<int:pk>/",
        PlanetDetailView.as_view(),
        name="planet-detail"
    ),

    path("planet/create/",
        PlanetCreateView.as_view(),
        name="planet-create"
    ),

    path(
        "planet/<int:pk>/delete/",
        PlanetDeleteView.as_view(),
        name="planet-delete",
    ),
    path(
        "planet/<int:pk>/update/",
        PlanetUpdateView.as_view(),
        name="planet-update",
    ),
]
