from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from vessel.inventory.api import InventoryViewSet
from vessel.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("inventory", InventoryViewSet)


app_name = "api"
urlpatterns = router.urls
