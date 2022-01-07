from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from vessel.inventory.api import ItemViewSet
from vessel.planets.api.views import PlanetViewSet
from vessel.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
# todo refactor to inventory/items
router.register("inventory", ItemViewSet)
router.register("planets", PlanetViewSet)


app_name = "api"
urlpatterns = router.urls
